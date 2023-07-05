```python
import bpy

# Clear all mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Define the bot model
def create_bot_model():
    # Create the main body of the bot
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
    body = bpy.context.object
    body.scale = (0.6, 0.3, 1.0)

    # Create the head of the bot
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 1.2))
    head = bpy.context.object
    head.scale = (0.4, 0.4, 0.4)

    # Create the eyes of the bot
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(-0.15, 0.2, 1.3))
    eye1 = bpy.context.object
    eye1.scale = (0.1, 0.1, 0.1)

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0.15, 0.2, 1.3))
    eye2 = bpy.context.object
    eye2.scale = (0.1, 0.1, 0.1)

    # Create the antenna of the bot
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.4, enter_editmode=False, align='WORLD', location=(0, 0, 1.6))

    # Join all parts to create the bot model
    bpy.ops.object.select_all(action='DESELECT')
    body.select_set(True)
    head.select_set(True)
    eye1.select_set(True)
    eye2.select_set(True)
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.join()

# Create the bot model
create_bot_model()
```