import os
import shutil

source_dir = 'static.wixstatic.com/media'
target_dir = 'website/images'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for root, dirs, files in os.walk(source_dir):
    for f in files:
        if f.endswith('.html') or f == 'index.html':
            continue
        filepath = os.path.join(root, f)
        # some files have weird extensions or names, just grab them
        # to avoid collisions, we can use the parent folder's name (which is the real hash name)
        # e.g. addb59_027f6a0f743f4fb785f78873381e280c_mv2.jpg
        parent_dir = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(filepath))))
        
        # let's find the original name, usually the top level directory name inside media/
        rel_path = os.path.relpath(filepath, source_dir)
        top_dir = rel_path.split(os.sep)[0]
        
        # top_dir is something like addb59_027f...mv2.jpg, which has extensions.
        if '.' in top_dir:
            file_name = top_dir
        else:
            file_name = f
            
        target_path = os.path.join(target_dir, file_name)
        
        # We only copy if we haven't already or if it's the largest file (highest resolution)
        # Since httrack makes multiple resolutions, let's keep the largest one.
        if os.path.exists(target_path):
            if os.path.getsize(filepath) > os.path.getsize(target_path):
                shutil.copy2(filepath, target_path)
        else:
            try:
                shutil.copy2(filepath, target_path)
            except Exception as e:
                pass

print(f"Copied {len(os.listdir(target_dir))} files.")
