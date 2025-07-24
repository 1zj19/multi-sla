import zipfile
import os
from io import BytesIO

def get_image_files(zf):
    """Returns a sorted list of valid image file names in the ZIP."""
    return sorted(
        [f for f in zf.namelist() if f.endswith(".png") and not f.startswith("__MACOSX")],
        key=lambda x: x.lower()
    )

def interleave_and_save(zip1_path, zip2_path, output_path):
    """Interleaves image files from two ZIPs and writes to a new ZIP file."""
    with zipfile.ZipFile(zip1_path, 'r') as zip1, zipfile.ZipFile(zip2_path, 'r') as zip2:
        files1 = get_image_files(zip1)
        files2 = get_image_files(zip2)

        # Interleave files
        interleaved = []
        for a, b in zip(files1, files2):
            interleaved.append(('a', a))
            interleaved.append(('b', b))
        # Add extras if one zip has more files
        for leftover in files1[len(files2):]:
            interleaved.append(('a', leftover))
        for leftover in files2[len(files1):]:
            interleaved.append(('b', leftover))

        # Create the output ZIP file
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as out_zip:
            for origin, filename in interleaved:
                data = zip1.read(filename) if origin == 'a' else zip2.read(filename)
                # Save in flat format: a_out0000.png, b_out0000.png, etc.
                short_name = os.path.basename(filename)
                new_name = f"{origin}_{short_name}"
                out_zip.writestr(new_name, data)

        print(f"✅ Interleaved zip saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    zip1_path = input("Enter path to first zip file: ")
    zip2_path = input("Enter path to second zip file: ")
    output_path = input("Enter output zip file name (e.g., interleaved.zip): ")
    interleave_and_save(zip1_path, zip2_path, output_path)
