package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem14499 {
	static int N;
	static int M;
	static int[][] map;
	static int[] dx = {0,0,-1,1};
	static int[] dy = {1,-1,0,0};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		int x= Integer.parseInt(str[2]);
		int y =Integer.parseInt(str[3]);
		int[] k = new int[Integer.parseInt(str[4])];
		map = new int[N][M];
		
		int dice1[] = new int[4];
		int dice2[] = new int[4];
		
		
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		str = br.readLine().split(" ");
		for(int i=0; i<k.length; i++) {
			k[i] = Integer.parseInt(str[i]);
		}
		
		int cursor[] = new int[2];
		cursor[0] = 0;
		cursor[1] = 1;
		for(int i=0; i<k.length; i++) {
			int nx = x+dx[k[i]-1];
			int ny = y+dy[k[i]-1];
			if(0<=nx && nx<N && 0<=ny && ny<M) {
				if (k[i] == 3 || k[i] == 4) {
					if(k[i]==3) {
						if(cursor[0]<3) {
							cursor[0]++;
						}else {
							cursor[0] = 0;
						}
					}else {
						if(cursor[0]>0) {
							cursor[0]--;
						}else {
							cursor[0]=3;
						}
					}
					if(map[nx][ny]==0) {
						map[nx][ny] = dice1[cursor[0]];
					}else if(map[nx][ny]!=0) {
						dice1[cursor[0]] = map[nx][ny];
						map[nx][ny] =0;
					}
					if(cursor[0]+2>3) {
						System.out.println(dice1[cursor[0]-2]);
						if(cursor[1]+2>3) {
							dice2[cursor[1]] =dice1[cursor[0]]; 
							dice2[cursor[1]-2] =dice1[cursor[0]-2]; 
						}else {
							dice2[cursor[1]] =dice1[cursor[0]]; 
							dice2[cursor[1]+2] =dice1[cursor[0]-2]; 
						}
					}else {
						System.out.println(dice1[cursor[0]+2]);
						if(cursor[1]+2>3) {
							dice2[cursor[1]] =dice1[cursor[0]]; 
							dice2[cursor[1]-2] =dice1[cursor[0]+2]; 
						}else {
							dice2[cursor[1]] =dice1[cursor[0]]; 
							dice2[cursor[1]+2] =dice1[cursor[0]+2]; 
						}
					}
				}
				else if(k[i]==1|| k[i] ==2) {
					if(k[i]==2) {
						if(cursor[1]<3) {
							cursor[1]++;
						}else {
							cursor[1] = 0;
						}
					}else {
						if(cursor[1]>0) {
							cursor[1]--;
						}else {
							cursor[1]=3;
						}
					}
					if(map[nx][ny]==0) {
						map[nx][ny] = dice2[cursor[1]];
					}else if(map[nx][ny]!=0) {
						dice2[cursor[1]] = map[nx][ny];
						map[nx][ny] =0;
					}
					if(cursor[1]+2>3) {
						System.out.println(dice2[cursor[1]-2]);
						if(cursor[0]+2>3) {
							dice1[cursor[0]] =dice2[cursor[1]]; 
							dice1[cursor[0]-2] =dice2[cursor[1]-2]; 
						}else {
							dice1[cursor[0]] =dice2[cursor[1]]; 
							dice1[cursor[0]+2] =dice2[cursor[1]-2]; 
						}
					}else {
						System.out.println(dice2[cursor[1]+2]);
						if(cursor[0]+2>3) {
							dice1[cursor[0]] =dice2[cursor[1]]; 
							dice1[cursor[0]-2] =dice2[cursor[1]+2]; 
						}else {
							dice1[cursor[0]] =dice2[cursor[1]]; 
							dice1[cursor[0]+2] =dice2[cursor[1]+2]; 
						}
					}
				}
				x = nx;
				y = ny;
			}
		}
	}

}


