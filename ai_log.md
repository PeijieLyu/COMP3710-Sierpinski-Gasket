# AI Usage Log

I used ChatGPT to help me understand and implement the Sierpinski Gasket.

## Prompt 1

**Prompt:**  
Can you explain how the Sierpinski Gasket binary address algorithm works? I don't really understand what `x AND (y-x) == 0` means.

**What I learned:**  
ChatGPT explained that `AND` is a bitwise operation. The binary digits of `x` and `y-x` are compared, and the result is used to decide whether a point belongs to the pattern. This helped me understand the main idea before writing the code.

## Prompt 2

**Prompt:**  
Can you teach me step by step how to generate this Sierpinski Gasket using PyTorch? 

**What I did:**  
I created the x and y coordinates as PyTorch tensors, used `torch.meshgrid()` to create the coordinate grid, and then used `torch.bitwise_and()` to apply the rule to all the coordinates. Finally, I converted the result back to the CPU and displayed it using Matplotlib.

## Follow-up

During the implementation I also asked some small questions about tensor shapes, `meshgrid`, GPU tensors and displaying the result with Matplotlib.