import zipfile
import os
from io import BytesIO

#CURRENTLY JUST combines the files, not interleaved.

def get_image_files(zf):
    """Returns a list of valid image file names in the ZIP."""
    return [f for f in zf.namelist() if f.endswith(".png") and not f.startswith("__MACOSX")]
    
def interleave_and_save(zip1_path, zip2_path, output_path):
    """Interleaves image files from two ZIPs and writes to a new ZIP file."""
    with zipfile.ZipFile(zip1_path, 'r') as zip1, zipfile.ZipFile(zip2_path, 'r') as zip2:
        files1 = get_image_files(zip1)
        files2 = get_image_files(zip2)

        # Interleave files
        interleaved = []
        for a, b in zip(files1, files2):
            interleaved.append(('a', a)) ## appends a tuple 
            interleaved.append(('b', b))
        # Add extras if one zip has more files
        for leftover in files1[len(files2):]: ## start at end len of other zip, add any extras
            interleaved.append(('a', leftover))
        for leftover in files2[len(files1):]: # does nothing if len(files1) > len(files2) ?
            interleaved.append(('b', leftover))
        ##CURRENTLY including a png image of the whole model, need to delete that manually or something b4 running this

        # Create the output ZIP file
        count = 0
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as out_zip:
            for origin, filename in interleaved:
                data = zip1.read(filename) if origin == 'a' else zip2.read(filename)
                # Save in flat format: a_out0000.png, b_out0000.png, etc.
                short_name = os.path.basename(filename)
                new_name = f"{count}_{short_name}"
                count+=1
                ##TODO 
                ##MACOS sort alphabetically by default, if filenumbering are same what happens? account for tthis
                out_zip.writestr(new_name, data)

        print(f"✅ Interleaved zip saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    zip1_path = input("Enter path to first zip file: ")
    zip2_path = input("Enter path to second zip file: ")
    output_path = input("Enter output zip file name (e.g., interleaved.zip): ")
    interleave_and_save(zip1_path, zip2_path, output_path)
