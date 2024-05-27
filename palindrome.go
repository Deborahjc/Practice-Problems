package main

func palindrome(n int) bool{
	num := n
	reverse := 0
	for num > 0{
		remainder := num % 10
		reverse = reverse * 10 + remainder
		num = num / 10
	}
	if reverse == n {
		return true
	}
	return false
}
