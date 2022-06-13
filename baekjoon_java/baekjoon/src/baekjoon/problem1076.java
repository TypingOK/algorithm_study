package baekjoon;

import java.util.Scanner;

public class problem1076 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = number(sc.nextLine());
		String b = number(sc.nextLine());
		int i = Integer.parseInt(a+b);
		int c = mul(sc.nextLine());
		System.out.println((long)i*c);
				
	}
	static String number(String s) {
		int a = 0;
		switch(s){
		case "black":
			break;
		case "brown":
			a=1;
			break;
		case "red":
			a=2;
			break;
		case "orange":
			a=3;
			break;
		case "yellow":
			a=4;
			break;
		case "green":
			a=5;
			break;
		case "blue":
			a=6;
			break;
		case "violet":
			a=7;
			break;
		case "grey":
			a=8;
			break;		
		case "white":
			a=9;
			break;
		}
		return Integer.toString(a);
	}
	static int mul(String s) {
		int a =1;
		switch(s) {
		case "black":
			break;
		case "brown":
			a=10;
			break;
		case "red":
			a=100;
			break;
		case "orange":
			a=1000;
			break;
		case "yellow":
			a=10000;
			break;
		case "green":
			a=100000;
			break;
		case "blue":
			a=1000000;
			break;
		case "violet":
			a=10000000;
			break;
		case "grey":
			a=100000000;
			break;		
		case "white":
			a=1000000000;
			break;
		}
		return a;
	}
}
