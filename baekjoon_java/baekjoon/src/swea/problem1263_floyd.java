package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class problem1263_floyd {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int TC = Integer.parseInt(br.readLine());
		StringTokenizer str;
		for(int tc=1; tc<=TC; tc++) {
			str = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(str.nextToken());
			
			int[][] map = new int[N][N];
			for(int i=0; i<N; ++i) {
				for(int j=0; j<N; ++j) {
					map[i][j] = Integer.parseInt(str.nextToken());
					if(i!=j && map[i][j] == 0) {
						map[i][j] = 9999999;
					}
				}
			}
			
			for(int k=0; k <N; ++k) { // 경로
				for(int i=0; i<N; ++i) { // 출발
					if(i==k) {
						continue;
					}
					for(int j=0; j<N; ++j) { // 도착
						if(i==j || j == k) {
							continue;
						}
						if(map[i][j]>map[i][k]+map[k][j]) {
							map[i][j] = map[i][k]+map[k][j];
						}
					}
				}
				for(int z=0; z<N; z++) {
					for(int j=0;j<N; j++) {
						System.out.print(map[z][j]+" ");
					}
					System.out.println();
				}
				System.out.println();
				System.out.println();
			}
			
			int min = Integer.MAX_VALUE;
			
			for(int i=0; i<N; i++) {
				int sum=0;
				for(int j=0; j<N; j++) {
					sum += map[i][j];
				}
				min = Math.min(min,sum);
			}
			System.out.println("#"+tc+" "+min);
			
		}
	}
	
}
