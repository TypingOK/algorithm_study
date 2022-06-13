package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class problem15662 {

	public static void main(String[] args) throws IOException{
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		
		LinkedList<Integer>[] test = new LinkedList[T];
		
		int[][] gear = new int[T][2];
		
		char c[];
		for(int i=0; i<T; i++) {
			test[i] = new LinkedList<Integer>();
			c = br.readLine().toCharArray();
			for(int j=0; j<8; j++) {
				test[i].add((int)c[j]-'0');
				if(j==2) {
					gear[i][0] = (int)c[j]-'0';
				}
				else if(j==6) {
					gear[i][1] = (int)c[j]-'0';
				}
			}
		}
		
		int K = Integer.parseInt(br.readLine());
		String str[];
		int N;
		int M;
		boolean flag;
		for(int i=0; i<K; i++) {
			flag= false;
			str = br.readLine().split(" ");
			N = Integer.parseInt(str[0])-1;
			M = Integer.parseInt(str[1]);
			int temp = M;
			if(M == -1) {
				test[N].add(test[N].pollFirst());
			} else if (M == 1) {
				test[N].addFirst(test[N].pollLast());
			}

			for (int j = N - 1; j >= 0; j--) {
				if (test[j].get(2) != gear[j + 1][1]) {
					if (M == 1) {
						test[j].add(test[j].pollFirst());
						M = -1;
					} else if (M == -1) {
						test[j].addFirst(test[j].pollLast());
						M = 1;
					}
					flag=true;
				} else {
					break;
				}
			}
			if(flag) {
				M = temp;
			}
			for (int j = N + 1; j <= T-1; j++) {
				if (test[j].get(6) != gear[j - 1][0]) {
					if (M == 1) {
						test[j].add(test[j].pollFirst());
						M = -1;
					} else if (M == -1) {
						test[j].addFirst(test[j].pollLast());
						M = 1;
					}
				} else {
					break;
				}
			}
			
			for(int j=0; j<T; j++) {
				gear[j][0] = test[j].get(2);
				gear[j][1] = test[j].get(6);
			}
			
//			for(int j=0; j<4; j++) {
//				for(int a=0; a<8; a++) {
//					System.out.print(test[j].get(a)+" ");
//				}
//				System.out.println();
//			}
//			System.out.println();
		}
		
		int answer =0;
		for(int i=0; i<T; i++) {
			if(test[i].get(0)== 1) {
				answer++;
			}
		}
		
		System.out.println(answer);
		
		
	}

}
