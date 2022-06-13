package baekjoon;

import java.math.BigInteger;
import java.util.Scanner;

public class problem1271 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		BigInteger a = scan.nextBigInteger();
		BigInteger b = scan.nextBigInteger();
		scan.close();
		System.out.println(a.divide(b));
		System.out.println(a.remainder(b));
	}

}
