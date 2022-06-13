package swea;

import java.util.Scanner;

public class swea1865 {
	static int N;
	static double[][] map;
	static boolean visit[];
	static double max;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for(int tc = 1; tc<=TC; tc++) {
			N = sc.nextInt();
			map = new double[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					map[i][j] = sc.nextInt()*0.01;
				}
			}
			
			max = Double.MIN_VALUE;
			visit = new boolean[N];
			comb(0,1,0);
			
			System.out.println("#"+tc+" "+String.format("%.6f", max));
		}
		
	}
	
	public static void comb(int depth,double sum,int x) {
		if(sum*100<=max) {
			return;
		}
		if(depth>=N) {
			sum *= 100;
			max = Math.max(max, sum);
			
			return;
		}
		for (int j = 0; j < N; j++) {
			if (!visit[j]) {
				visit[j] = true;
				comb(depth+1,sum*map[x][j],x+1);
				visit[j] = false;
			}
		}
	}

}
