import cx_Freeze
#cx freez script for exe file
executables = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
    name="Dzavolcici",
    options={
        "build_exe": {"packages": ["pygame"],
        "include_files": [
            "block1.png",
            "devil.png",
            "angel.png",
            "h1.jpg",
            "satan.jpg",
            "anvil.jpg"]
        },
    },
    executables=executables
)

#python setup.py build