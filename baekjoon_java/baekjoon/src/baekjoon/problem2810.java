package baekjoon;

import java.util.*;
public class problem2810 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		char[] str = sc.next().toCharArray();
		int num=0;
		for(int i=0; i<N; i++) {
			if(str[i]=='S') {
				num++;
			}else if(str[i] == 'L') {
				num++;
				i++;
			}
		}
		num++;
		if(num-N>=0) {
			System.out.println(N);
		}else {
			System.out.println(num);
		}
	}

}
