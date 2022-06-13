package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem5656 {
	
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int N,W,H;
	static int[][] map;
	static int min;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int TC = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=TC; tc++) {
			int[][] copy;
			min = Integer.MAX_VALUE;
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			map = new int[H][W];
			copy = new int[H][W];
			for(int i=0; i<H; i++) {
				st = new StringTokenizer(br.readLine()," ");
				for(int j=0; j<W; j++) {
					copy[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			perm(copy,0);
			System.out.println("#"+tc+" "+min);
		}
	}
	
	public static void perm(int [][]map,int index) {
		int result = find(map);
		if(result==0) {
			min = 0;
			return;
		}
		if(index == N) {
			min = Math.min(result,min);
			return ;
		}
		int newMap[][] =new int[H][W];
		for(int i=0; i<W; i++) {
			int depth = -1;
			for(int j=0; j<H; j++) {
				if(map[j][i] >=1) {
					depth = j;
					break;
				}
			}
			if(depth == -1) {
				continue;
			}
			copyMap(map,newMap);
			int cnt = newMap[depth][i];
			Boom(depth,i,newMap,cnt);
			drop(newMap);
			perm(newMap,index+1);
			
		}
	}
	
	
	public static void Boom(int x, int y,int[][] test, int cnt) {
		test[x][y] = 0;
		for(int i=0; i<4; i++) {
			for(int j=1; j<cnt; j++) {
				int nx = x+dx[i]*j;
				int ny = y+j*dy[i];
				if(0 <= nx && nx<H && 0<=ny && ny<W) {
					if(test[nx][ny] > 1) {
						int nextCnt= test[nx][ny];
						Boom(nx,ny,test,nextCnt);
						
					}else if(test[nx][ny]==1) {
						test[nx][ny]=0;
					}
				}
			}
		}
	}
	
	public static void drop(int [][] map) {
		for(int i=0; i<W; i++) {
			int r= H-1;
			while(r>0) {
				if(map[r][i]==0) { // 빈칸이면 내릴 벽돌찾기
					int nr = r-1;
					while(nr>0 && map[nr][i]==0) nr--;
					
					map[r][i] = map[nr][i];
					map[nr][i]=0;
				}
				r--;
			}
		}
	}
	
	public static int find(int[][] copy) {
		int sum =0;
		for(int i=0; i<H; i++) {
			for(int j=0; j<W; j++) {
				if(copy[i][j]!=0) {
					sum++;
				}
			}
		}
		return sum;
	}
	static void copyMap(int[][] map, int[][] newMap) {
		for(int i=0; i<H; i++) {
			for(int j=0; j<W; j++) {
				newMap[i][j] = map[i][j];
			}
		}
	}
}
