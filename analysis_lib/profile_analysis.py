import cProfile
import pstats
import io
from analysis_lib.__main__ import main

def profile():
    pr = cProfile.Profile()
    pr.enable()

    main()  

    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats()

    with open("profiling_result.txt", "w") as f:
        f.write(s.getvalue())

if __name__ == "__main__":
    profile()
