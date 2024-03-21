def toko_buah(*args):
	print("Toko Buah Koperasi UNJANI Yogyakarta")
	buah = int(input("Masukan buah yang dibeli : "))

	for i in range(buah):
		buah = input(f"Buah {i+1} : ")
		args += (buah,)

		print("Buah yang anda beli adalah : ")
		for i, buah in enumerate (args):
			print(f"{i+1}. {buah}")
	print("Terimakasih")

toko_buah()