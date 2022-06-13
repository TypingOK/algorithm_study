package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class problem1767 {
	static int N, max,totalCnt,min,map[][];
	static int[] dx= {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static ArrayList<int[]> list;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int TC = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=TC; tc++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			list = new ArrayList<int[]> ();
			max = 0;
			min = Integer.MAX_VALUE;
			totalCnt=0;
			
			for(int i=0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine()," ");
				for(int j=0; j<N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if((i==0||i==N-1||j==0||j==N-1) && map[i][j] == 1) continue;
					if(map[i][j] ==1) {
						list.add(new int[] {i,j});
						totalCnt++;
					}
				}
			}
			go(0,0);
			
			System.out.println("#"+tc+" "+min);
		}
		
	}
	private static void go (int index,int cCnt) {
		if(index==totalCnt) {
			int res = getLength();
			if(max < cCnt) {
				max = cCnt;
				min = res;
			}else if(max == cCnt) {
				if(min>res) min = res;
			}
			
			return ;
		}
		
		int[] core = list.get(index);
		int r = core[0];
		int c = core[1];
		
		//전선을 놓아보기(4방향으로 )
		for(int d=0; d<4; d++) {
			if(isAvailable(r,c,d)) { // 현재 코어의 r,c 위치에서 d 방향으로 전선을 놓을 수 있다면
				setStatus(r,c,d,2); //전선 놓기
				go(index+1,cCnt+1);
				setStatus(r,c,d,0); // 전선 지우기
			}
		}
		//전선을 놓지 않기
		go(index+1, cCnt);
	}
	private static boolean isAvailable(int r, int c, int d) {
		int nr = r, nc = c;
		while(true) {
			nr += dx[d];
			nc += dy[d];
			if(nr<0 || nr >=N || nc<0 || nc>= N) break;
			//다른 코어나 전선을 만나면 return false;
			if(map[nr][nc] >=1 )return false;
		}
		return true;
	}
	private static void setStatus(int r,int c, int d, int s) { //r,c, 위치에서 d 방향으로 전선을 놓거나(2) 지우거나(0)
		int nr = r, nc = c;
		while(true) {
			nr += dx[d];
			nc += dy[d];
			
			if(nr<0 || nr >=N || nc<0 || nc>= N) break;
			map[nr][nc] = s;
		}
	}
	private static int getLength() {
		int lCnt = 0;
		for(int r= 0; r<N; r++) {
			for(int c=0; c<N; c++) {
				if(map[r][c] ==2 ) lCnt++;
			}
		}
		return lCnt;
	}
}
