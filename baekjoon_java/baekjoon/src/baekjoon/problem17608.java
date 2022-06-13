package baekjoon;

import java.util.Scanner;

public class problem17608 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] stack = new int[n];
		for(int i=0; i<n; i++) {
			stack[i] = sc.nextInt();
		}
		int count=1;
		int max = stack[n-1];
		for(int i=n-2; i>=0; i--) {
			if(max<stack[i]) {
				max=stack[i];
				count++;
			}
		}
		System.out.println(count);
	}
}
