package baekjoon;

import java.util.Scanner;

public class problem1233 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int[] cnt = new int [100000];
		for(int i=1;i<=a;i++) {
			for(int j=1; j<=b; j++) {
				for(int k=1; k<=c; k++) {
					cnt[i+j+k]++;
				}
			}
		}
		int max=0;
		int index=cnt.length;
		for(int i=cnt.length-1; i>=0; i--) {
			max=Math.max(max, cnt[i]);
			if(max==cnt[i]) {
				if(index>i) {
					index=i;					
				}
			}
		}
		System.out.println(index);
	}

}
