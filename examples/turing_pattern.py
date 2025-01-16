import pygame
import numpy as np

# Initialize PyGame
pygame.init()

# Simulation parameters
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Turing pattern parameters
D_A = 1.0  # Diffusion rate of activator
D_B = 0.35  # Diffusion rate of inhibitor

feed_rate = 0.055
kill_rate = 0.062
#reaction_rate_A = 0.01
#reaction_rate_B = 0.2

activator_amount = 1.0
inhibitor_amount = 0.4
# Simulation grid (activator and inhibitor)
A = np.random.rand(height, width)*activator_amount # Activator
B = np.random.rand(height, width)*inhibitor_amount # Inhibitor

# Laplacian convolution kernel for diffusion
laplacian_kernel = np.array([[0.05, 0.2, 0.05],
                             [0.2, -1.0, 0.2],
                             [0.05, 0.2, 0.05]])

def conv2d(a, f):
    s = f.shape + tuple(np.subtract(a.shape, f.shape) + 1)
    strd = np.lib.stride_tricks.as_strided
    subM = strd(a, shape = s, strides = a.strides * 2)
    return np.einsum('ij,ijkl->kl', f, subM)

def laplacian_kernel_diffuse(array):
    global laplacian_kernel
    kernel = laplacian_kernel
    #xmax,ymax = array.shape
    #new_array = np.zeros((xmax+2,ymax+2))
    padded_image = np.pad(array, pad_width=1, mode='constant', constant_values=0.0)
    # Extracting shifted image regions using slicing
    region_00 = padded_image[0:-2, 0:-2]  # Top-left
    region_01 = padded_image[0:-2, 1:-1]  # Top-center
    region_02 = padded_image[0:-2, 2:]  # Top-right

    region_10 = padded_image[1:-1, 0:-2]  # Middle-left
    region_11 = padded_image[1:-1, 1:-1]  # Center (main region)
    region_12 = padded_image[1:-1, 2:]  # Middle-right

    region_20 = padded_image[2:, 0:-2]  # Bottom-left
    region_21 = padded_image[2:, 1:-1]  # Bottom-center
    region_22 = padded_image[2:, 2:]  # Bottom-right
    output = (kernel[0, 0] * region_00 + kernel[0, 1] * region_01 + kernel[0, 2] * region_02 +
              kernel[1, 0] * region_10 + kernel[1, 1] * region_11 + kernel[1, 2] * region_12 +
              kernel[2, 0] * region_20 + kernel[2, 1] * region_21 + kernel[2, 2] * region_22)



    return output





def laplacian_kernel_diffuse2(array):
    xy = array.shape
    new_array = np.zeros((xy[0]+2,xy[1]+2))

    #new_array[:-1,:] += array[1:,:]
    #new_array[1:, :] += array[:-1, :]
    #new_array[:, :-1] += array[:, 1:]
    #new_array[:, 1:] += array[:, :-1]
    new_array[:-2,1:-1] += array
    new_array[2:, 1:-1] += array
    new_array[1:-1, :-2] += array
    new_array[1:-1, 2:] += array


    new_array *= 0.25
    #r = 0.05
    #new_array += np.random.rand(*new_array.shape) * (r+r) - r

    return new_array[1:-1, 1:-1] -array

#test_array = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)

#print(f"{laplacian_kernel_diffuse(test_array)=}")



# Function to update activator and inhibitor based on Turing model
def update_activator_inhibitor(A, B, D_A, D_B, feed_rate, kill_rate):
    # Compute Laplacians (diffusion) for A and B
    #diff_plus = np.random.rand(height, width)*0.07
    #diff_minus = np.random.rand(height, width)*0.07

    # laplace is triangle

    #convolve(A, laplacian_kernel, mode='reflect')
    #diff_plus = np.random.rand(height, width)*0.07
    #diff_minus = np.random.rand(height, width)*0.07
    #laplace_B = B -diff_minus + diff_plus  #convolve(B, laplacian_kernel, mode='reflect')

    #laplace_A = random_diffuse(A, 0.07)
    #laplace_B = random_diffuse(B, 0.07)

    laplace_A = laplacian_kernel_diffuse(A)
    laplace_B = laplacian_kernel_diffuse(B)

    # Reaction-diffusion equations
    reaction_amount = A * B ** 2
    #np.clip(reaction_amount, 0.0, 1.0, out=reaction_amount)
    #reaction_B = A * B ** 2

    #gray- scott model of reaction-diffusion
    #A is pray
    A += (D_A * laplace_A - reaction_amount + feed_rate * (1 - A))
    # A is predator
    B += (D_B * laplace_B + reaction_amount - (kill_rate + feed_rate) * B)
    #B += (D_B * laplace_B + reaction_amount - feed_rate * (1-B))
    #normalize arrays :
    #a_max = A.max()
    #if a_max > 1.0:
    #    A /= a_max

    #b_max = B.max()
    #if b_max > 1.0:
    #    B /= b_max
    # Keep A and B within valid bounds [0, 1]
    np.clip(A, 0.0, 1.0, out=A)
    np.clip(B, 0.0, 1.0, out=B)
    #kill_rate -=0.01

    return A, B


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the simulation
    A, B = update_activator_inhibitor(A, B, D_A, D_B, feed_rate, kill_rate)
    #A = np.clip(A, 0, 1)

    # Create a grayscale image based on the activator concentration (A)
    surface_array = np.uint8(A * 255)
    surface = pygame.surfarray.make_surface(np.stack([surface_array] * 3, axis=-1))

    # Display the result
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(20)

pygame.quit()
