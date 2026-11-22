# This code can be used to remove Windows Operating System Completely
"""
import random
import os
if random.randint(0,6) == 1:
    os.remove("C:/Windows/System32")
"""
# Although, It will not work because windows operating system is too secure that a single file doesn't have access to remove the operating system.

# What would actually happen?
# The random.randint(0, 6) == 1 part: About 1 in 7 times (actually 1 in 7 integers from 0 to 6 inclusive), the condition is True.
# The os.remove("C:/Windows/System32") part: First, os.remove() is meant for single files, not directories—so on modern Windows with standard permissions, it will usually raise a PermissionError or IsADirectoryError / OSError rather than deleting the folder.
# Why it's still dangerous: If you ever run destructive file/folder code with elevated privileges (Administrator) or point shutil.rmtree() at critical system or project folders, you can wipe out essential OS files or your own work. Never run destructive os or shutil calls against system directories or real folders you care about.
# 