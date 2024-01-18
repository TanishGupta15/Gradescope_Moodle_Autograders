import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
import subprocess
from timeout_decorator import timeout

unittest.TestCase.maxDiff = None

class CorpusQnATool(unittest.TestCase):
	def setUp(self):
		self.test_cases = []

	@weight(2.5)
	@number("1")
	@timeout(40*60)
	def test_case_1(self):
		with open("query_1.txt", "r") as f:
			# read and print first line
			test_case_1 = f.readline()
			print("Running query:")
			print(test_case_1)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_1.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-1 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-1 Failed")

			print(out)
			print(err)
			self.fail("Test Case-1 Failed")


	@weight(2.5)
	@number("2")
	@timeout(40*60)
	def test_case_2(self):
		with open("query_2.txt", "r") as f:
			# read and print first line
			test_case_2 = f.readline()
			print("Running query:")
			print(test_case_2)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_2.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-2 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-2 Failed")

			print(out)
			print(err)
			self.fail("Test Case-2 Failed")


	@weight(2.5)
	@number("3")
	@timeout(40*60)
	def test_case_3(self):
		with open("query_3.txt", "r") as f:
			# read and print first line
			test_case_3 = f.readline()
			print("Running query:")
			print(test_case_3)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_3.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-3 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-3 Failed")

			print(out)
			print(err)
			self.fail("Test Case-3 Failed")


	@weight(2.5)
	@number("4")
	@timeout(40*60)
	def test_case_4(self):
		with open("query_4.txt", "r") as f:
			# read and print first line
			test_case_4 = f.readline()
			print("Running query:")
			print(test_case_4)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_4.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-4 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-4 Failed")

			print(out)
			print(err)
			self.fail("Test Case-4 Failed")


	@weight(2.5)
	@number("5")
	@timeout(40*60)
	def test_case_5(self):
		with open("query_5.txt", "r") as f:
			# read and print first line
			test_case_5 = f.readline()
			print("Running query:")
			print(test_case_5)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_5.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-5 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-5 Failed")

			print(out)
			print(err)
			self.fail("Test Case-5 Failed")


	@weight(2.5)
	@number("6")
	@timeout(40*60)
	def test_case_6(self):
		with open("query_6.txt", "r") as f:
			# read and print first line
			test_case_6 = f.readline()
			print("Running query:")
			print(test_case_6)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_6.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-6 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-6 Failed")

			print(out)
			print(err)
			self.fail("Test Case-6 Failed")


	@weight(2.5)
	@number("7")
	@timeout(40*60)
	def test_case_7(self):
		with open("query_7.txt", "r") as f:
			# read and print first line
			test_case_7 = f.readline()
			print("Running query:")
			print(test_case_7)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_7.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-7 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-7 Failed")

			print(out)
			print(err)
			self.fail("Test Case-7 Failed")


	@weight(2.5)
	@number("8")
	@timeout(40*60)
	def test_case_8(self):
		with open("query_8.txt", "r") as f:
			# read and print first line
			test_case_8 = f.readline()
			print("Running query:")
			print(test_case_8)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_8.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-8 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-8 Failed")

			print(out)
			print(err)
			self.fail("Test Case-8 Failed")


	@weight(2.5)
	@number("9")
	@timeout(40*60)
	def test_case_9(self):
		with open("query_9.txt", "r") as f:
			# read and print first line
			test_case_9 = f.readline()
			print("Running query:")
			print(test_case_9)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_9.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-9 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-9 Failed")

			print(out)
			print(err)
			self.fail("Test Case-9 Failed")


	@weight(2.5)
	@number("10")
	@timeout(40*60)
	def test_case_10(self):
		with open("query_10.txt", "r") as f:
			# read and print first line
			test_case_10 = f.readline()
			print("Running query:")
			print(test_case_10)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_10.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-10 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-10 Failed")

			print(out)
			print(err)
			self.fail("Test Case-10 Failed")


	@weight(2.5)
	@number("11")
	@timeout(40*60)
	def test_case_11(self):
		with open("query_11.txt", "r") as f:
			# read and print first line
			test_case_11 = f.readline()
			print("Running query:")
			print(test_case_11)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_11.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-11 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-11 Failed")

			print(out)
			print(err)
			self.fail("Test Case-11 Failed")


	@weight(2.5)
	@number("12")
	@timeout(40*60)
	def test_case_12(self):
		with open("query_12.txt", "r") as f:
			# read and print first line
			test_case_12 = f.readline()
			print("Running query:")
			print(test_case_12)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_12.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-12 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-12 Failed")

			print(out)
			print(err)
			self.fail("Test Case-12 Failed")


	@weight(2.5)
	@number("13")
	@timeout(40*60)
	def test_case_13(self):
		with open("query_13.txt", "r") as f:
			# read and print first line
			test_case_13 = f.readline()
			print("Running query:")
			print(test_case_13)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_13.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-13 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-13 Failed")

			print(out)
			print(err)
			self.fail("Test Case-13 Failed")


	@weight(2.5)
	@number("14")
	@timeout(40*60)
	def test_case_14(self):
		with open("query_14.txt", "r") as f:
			# read and print first line
			test_case_14 = f.readline()
			print("Running query:")
			print(test_case_14)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_14.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-14 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-14 Failed")

			print(out)
			print(err)
			self.fail("Test Case-14 Failed")


	@weight(2.5)
	@number("15")
	@timeout(40*60)
	def test_case_15(self):
		with open("query_15.txt", "r") as f:
			# read and print first line
			test_case_15 = f.readline()
			print("Running query:")
			print(test_case_15)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_15.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-15 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-15 Failed")

			print(out)
			print(err)
			self.fail("Test Case-15 Failed")


	@weight(2.5)
	@number("16")
	@timeout(40*60)
	def test_case_16(self):
		with open("query_16.txt", "r") as f:
			# read and print first line
			test_case_16 = f.readline()
			print("Running query:")
			print(test_case_16)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_16.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-16 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-16 Failed")

			print(out)
			print(err)
			self.fail("Test Case-16 Failed")


	@weight(2.5)
	@number("17")
	@timeout(40*60)
	def test_case_17(self):
		with open("query_17.txt", "r") as f:
			# read and print first line
			test_case_17 = f.readline()
			print("Running query:")
			print(test_case_17)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_17.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-17 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-17 Failed")

			print(out)
			print(err)
			self.fail("Test Case-17 Failed")


	@weight(2.5)
	@number("18")
	@timeout(40*60)
	def test_case_18(self):
		with open("query_18.txt", "r") as f:
			# read and print first line
			test_case_18 = f.readline()
			print("Running query:")
			print(test_case_18)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_18.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-18 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-18 Failed")

			print(out)
			print(err)
			self.fail("Test Case-18 Failed")


	@weight(2.5)
	@number("19")
	@timeout(40*60)
	def test_case_19(self):
		with open("query_19.txt", "r") as f:
			# read and print first line
			test_case_19 = f.readline()
			print("Running query:")
			print(test_case_19)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_19.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-19 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-19 Failed")

			print(out)
			print(err)
			self.fail("Test Case-19 Failed")


	@weight(2.5)
	@number("20")
	@timeout(40*60)
	def test_case_20(self):
		with open("query_20.txt", "r") as f:
			# read and print first line
			test_case_20 = f.readline()
			print("Running query:")
			print(test_case_20)

		subprocess.run(["make"], check=True)
		self.bin_a = subprocess.Popen(["./qna_tool"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		query_file = "query_20.txt"
		out, err = self.bin_a.communicate(input=query_file)
		chk_str = "Passed\n"
		# if out == chk_str then print chk_str else print err
		if(out == chk_str):
			print("Yay, Passed :)")
		else:
			if(len(out) == 0):
				print("Failed :(")
				print("Your code did not print / return anything.")
				self.fail("Test Case-20 Failed")

			if(err.startswith("Passed")):
				print("Possibly, some cout statements are present in your code. Please remove them and try again.")
				out = out[:-7]
				print(out)
				self.fail("Test Case-20 Failed")

			print(out)
			print(err)
			self.fail("Test Case-20 Failed")