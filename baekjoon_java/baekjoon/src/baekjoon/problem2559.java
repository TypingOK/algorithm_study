package baekjoon;

import java.util.Scanner;

public class problem2559 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] number = new int[N];
		
		for(int i=0; i<N; i++) {
			number[i] = sc.nextInt();
		}
		int max = Integer.MIN_VALUE;
		if(N==K) {
			int temp =0;
			for(int i=0; i<N; i++) {
				temp+=number[i];
			}
			max = Math.max(max, temp);
		}else {
			for(int i=0; i<=N-K;i++) {
				int temp =0;
				for(int j=i; j<i+K; j++) {
					temp+=number[j];
				}
				max = Math.max(max, temp);
			}
		}
		System.out.println(max);
	}

}
