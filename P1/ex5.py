from Seq1 import Seq , generate_series
print("-----| Practice 1, Exercise 5 |------")


s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1 (Length:{Seq.len(s1)}): {s1} ")
Seq.count_bases(s1)
print(f"Sequence 1 (Length:{Seq.len(s2)}): {s2} ")
s2.count_bases()
print(f"Sequence 1 (Length:{Seq.len(s3)}): {s3} ")
Seq.count_bases(s3)