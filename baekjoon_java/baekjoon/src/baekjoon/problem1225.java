package baekjoon;

import java.util.Scanner;

public class problem1225 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		int lengthA = a.length();
		int lengthB = b.length();
		long sum=0;
		int[] arr=new int[lengthA];
		int[] arr2 = new int[lengthB];
		for(int i=0; i<lengthA; i++) {
			arr[i]=a.charAt(i)-'0';
		}
		for(int i=0; i<lengthB; i++) {
			arr2[i]=b.charAt(i)-'0';
		}
		for(int i=0; i<lengthA; i++) {
			for(int j=0; j<lengthB; j++) {
				sum+=(arr[i]*arr2[j]);
			}
		}
		System.out.println(sum);
	}

}
