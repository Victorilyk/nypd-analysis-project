import cProfile
import pstats
import io
import sys
from analysis_lib.__main__ import main

def profile():
    sys.argv = [
        "profile_analysis.py",
        "--input_dir", "my_data/",
        "--output_file", "profiling/profiling_output.csv"
    ]

    pr = cProfile.Profile()
    pr.enable()

    main()  

    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats()

    with open("profiling/profiler_output.txt", "w") as f:
        f.write(s.getvalue())

if __name__ == "__main__":
    profile()
