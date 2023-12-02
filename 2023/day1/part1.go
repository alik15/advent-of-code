package main

import (
	"fmt"
	"os"
	"strings"
)

func readlines(newfile string) []string {
	content, err := os.ReadFile(newfile)
	if err != nil {
	}
	lines := strings.Split(string(content), "\n")
	return lines
}

func Concatenate(digit1 int, digit2 int) int {
	digit1 = digit1*10 + digit2
	return digit1
}

func IsInt(c rune) bool {
	return c >= '0' && c <= '9'
}
func RuneToInt(c rune) int {
	num := 0
	num = int(c - '0')

	return num
}
func main() {
	data := readlines("puzzleinput.txt")
	var sum int = 0
	for _, str := range data {

		var num int = 0
		for _, c := range str {
			//fmt.Printf("%c", c)
			if IsInt(c) {
				if num == 0 {
					num = RuneToInt(c)
				} else {

					if num <= 9 {
						num = Concatenate(num, RuneToInt(c))
					} else if num > 9 {
						num = num / 10
						num = Concatenate(num, RuneToInt(c))
					}

				}
			}
		}
		if num <= 9 {
			num = Concatenate(num, num)
		}
		sum = sum + num
		fmt.Println(sum)
	}

}
