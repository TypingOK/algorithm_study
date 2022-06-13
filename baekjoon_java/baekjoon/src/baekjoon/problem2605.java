package baekjoon;

import java.util.*;
public class problem2605 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] number=new int[N];
		int[] answer = new int[N];
		for(int i=0; i<N; i++) {
			number[i] = sc.nextInt();
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<N-number[i]-1; j++) {
				answer[j]=answer[j+1];
			}
			answer[N-number[i]-1]=i+1;

		}
		for(int i=0; i<N; i++) {
			System.out.print(answer[i]+" ");
		}
			
	}

}
