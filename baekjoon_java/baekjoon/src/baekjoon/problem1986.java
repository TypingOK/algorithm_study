package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1986 {

	static int[] dx = {-1,1,2,2,1,-1,-2,-2};
	static int[] dy = {-2,-2,-1,1,2,2,1,-1};
	static int N;
	static int M;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] map;
		String[] str = br.readLine().split(" ");
		 N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		map = new int[N][M];
		for(int i=1; i<=3; i++) {
			str = br.readLine().split(" ");
			int[] temp = new int[2];
			int a = Integer.parseInt(str[0]);
			for(int j=1; j<str.length; j+=2) {
				temp[0]=Integer.parseInt(str[j])-1;
				temp[1]=Integer.parseInt(str[j+1])-1;
				map[temp[0]][temp[1]]=i;
			}
		}
		for(int i=0; i<N; i++){
			for(int j=0; j<M; j++) {
				if(map[i][j]==1) {
					queenMove(map,i,j);
				}else if(map[i][j]==2) {
					knightMove(map,i,j);
				}
			}
		}
		int cnt=0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(map[i][j]==0) {
					cnt++;
				}
			}
		}
//		for(int i=0; i<N; i++) {
//			for(int j=0; j<M; j++) {
//				System.out.print(map[i][j]+" ");
//			}
//			System.out.println();
//		}
		System.out.println(cnt);
	}
	static void knightMove(int[][] map,int x,int y) {
		for(int i=0; i<dx.length; i++) {
			int nx=x+dx[i];
			int ny=y+dy[i];
			if(0<=nx && nx<N &&0<=ny && ny<M &&map[nx][ny]==0 ) {
				map[nx][ny]=-1;
			}
		}
	}
	
	static void queenMove(int[][] map,int x, int y) {
		//대각선 아래
		boolean flag = false;
//		for(int k=0; k<N; k++) {
//			for(int l=0; l<M; l++) {
//				System.out.print(map[k][l]+" ");
//			}
//			System.out.println();
//		}
//		System.out.println();
		
		for(int i=1; i<Math.max(N,M); i++) {
			if(i+x<N && y+i<M&&map[x+i][y+i]==0) {
				map[x+i][y+i]=-1;
			}else if(i+x<N && y+i<M&& map[x+i][y+i]>=1) {
				break;
			}else if(x+i>=N && y+i>=M) {
				break;
			}
		}
		for(int i=y+1; i< M; i++) {
			if(map[x][i]>0) {
				break;
			}
			if(map[x][i]==0) {
				map[x][i]=-1;
			}
		}
		for(int i=1; i<Math.max(N, M); i++) {
			if(x-i>=0 && y+i<M && map[x-i][y+i]==0) {
				map[x-i][y+i] =-1;
			}else if(x-i>=0 && y+i<M &&map[x-i][y+i]>=1) {
				break;
			}else if(x-i<0 && y+i>=M) {
				break;
			}
		}
		for(int i=x+1; i<N; i++) {
			if(map[i][y]>0) {
				break;
			}else if(map[i][y]==0) {
				map[i][y]=-1;
			}
		}
		for(int i=1; i<Math.max(N, M); i++) {
			if(i+x<N && y-i>=0 &&map[i+x][y-i]==0) {
				map[i+x][y-i]=-1;
			}
			else if(i+x<N && y-i>=0 &&map[i+x][y-i]>=1) {
				break;
			}else if(i+x>=N && y-i<0){
				break;
			}
		}
		
		for(int i=y-1; i>=0; i--) {
			if(map[x][i]>0) {
				break;
			}else if(map[x][i]==0) {
				map[x][i]=-1;
			}
		}
		
		for(int i=1; i<Math.max(N, M); i++) {
			if(x-i>=0 && y-i>=0 && map[x-i][y-i]>0) {
				break;
			}
			else if(x-i>=0 && y-i>=0 && map[x-i][y-i]==0) {
				map[x-i][y-i]=-1;
			}else if(x-i<0 && y-i<0) {
				break;
			}
		}
		
		for(int i=x-1; i>=0; i--) {
			if(map[i][y]>0) {
				break;
			}else if(map[i][y]==0) {
				map[i][y]=-1;
			}
		}
	}
}
