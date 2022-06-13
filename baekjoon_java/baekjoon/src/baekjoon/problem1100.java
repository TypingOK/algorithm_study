package baekjoon;

import java.util.Scanner;

public class problem1100 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[][] c = new char[8][8];
		for(int i=0; i<8; i++) {
			String str = sc.nextLine();
			c[i] = str.toCharArray();
		}
		int cnt=0;
		for(int i=0; i<8; i++) {
			for(int j=0; j<8; j++) {
				if(i%2==0) {
					if(j%2==0 && c[i][j]=='F') {
						cnt++;
					}
				}
				else if (i%2==1) {
					if(j%2==1 && c[i][j]=='F') {
						cnt++;
					}
				}
			}
		}
		System.out.println(cnt);
	}

}
