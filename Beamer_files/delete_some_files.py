
import os
import glob
print("Hello, Python is working!")
# Specify the folder path
folder_paths = [    r"C:\Users\hhoumsi1\Documents\PhD-defense\Beamer_files", 
                    r"C:\Users\hhoumsi1\Documents\PhD-defense\Beamer_files\build", 
                    r"C:\Users\hhoumsi1\Documents\PhD-defense\Beamer_files\pictures",
                    #r"C:\Users\hhoumsi1\Documents\Redaction_these\Template_These_HibaH\Chapitres\Chapitre_1",
                    #r"C:\Users\hhoumsi1\Documents\Redaction_these\Template_These_HibaH\Chapitres\Chapitre_2"
]
# List of file patterns to delete
file_patterns = [
    "*.mtc", "*.log", "*.maf", "*.out", "*.lof", "*.dvi", "*.lot","*.mtc0","*.mtc1","*.mtc2","*.mtc3","*.mtc4","*.mtc5","*.mtc6","*.mtc7","*.mtc8","*.mtc9","*.mtc10","*.mtc11" ,"*.mtc12","*.mtc13","*.mtc14","*.mtc15","*.mtc16","*.mtc17","*.mtc18","*.mtc19","*.ps", "*.xml", "*.aux","*-blx.bib", "*.toc","*.ist", "*.glg", "*.glo", "*.gls", "*.acn", "*.acr", "*.alg", "*.xdy", "*.tex.bak", "*.sav.bak","*.sty.bak","*.cls.bak", "*.bib.bak","*.nlo","*.nav", "*.snm"
]

for folder_path in folder_paths:
    print(f"Processing folder: {folder_path}")
    
    # Loop through each file pattern
    for pattern in file_patterns:
        # Generate the full file path with the pattern
        files_to_delete = glob.glob(os.path.join(folder_path, pattern))
        
        # Delete matching files
        for file in files_to_delete:
            try:
                os.remove(file)  # Delete the file
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

print("Deletion process complete.")