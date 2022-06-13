package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class problem2309 {
	static int[] nan;
	static boolean[] select;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		nan = new int[9];
		int sum=0;
		for(int i=0; i<9; i++) {
			nan[i] = sc.nextInt();
			sum+=nan[i];
		}
		Arrays.sort(nan);
		for(int i=0; i<9; i++) {
			for(int j=i+1; j<9; j++) {
				if(sum-nan[i]-nan[j]==100) {
					for(int k=0; k<9; k++) {
						if(k!=i && k!=j) {
							System.out.println(nan[k]);
						}
					}
					System.exit(0);
				}
			}
		}
		
	}
}
