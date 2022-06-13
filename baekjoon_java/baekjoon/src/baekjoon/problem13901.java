package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem13901 {
	
	static int dx[] = {-1,1,0,0};
	static int dy[] = {0,0,-1,1};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		
		int N = Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		
		int[][] map = new int[N][M];
		boolean[][] visited = new boolean[N][M];
		
		str = br.readLine().split(" ");
		int K = Integer.parseInt(str[0]);
		int x=-1;
		int y=-1;
		for(int i=0; i<K; i++) {
			str = br.readLine().split(" ");
			map[Integer.parseInt(str[0])][Integer.parseInt(str[1])]=-1;
		}
		
		str = br.readLine().split(" ");
		map[Integer.parseInt(str[0])][Integer.parseInt(str[1])]=1;
		x=Integer.parseInt(str[0]);
		y=Integer.parseInt(str[1]);
		visited[Integer.parseInt(str[0])][Integer.parseInt(str[1])] = true;
		
		
		str = br.readLine().split(" ");
		int [] dnlcl = new int[4];
		for(int i=0; i<4; i++) {
			dnlcl[i]=Integer.parseInt(str[i])-1;
		}
		
		int index=0;
		int cnt=0;
		while(true) {
			
			int nx = x+dx[dnlcl[index]];
			int ny = y+dy[dnlcl[index]];
			
			if(0<=nx && nx<N && 0<=ny && ny<M && !visited[nx][ny] && map[nx][ny]!=-1) {
				visited[nx][ny] =true;
				map[x][y] = 0;
				x=nx;
				y = ny;
				map[x][y]=1;
				cnt=0;
			}else {
				index++;
				if(index==4) {
					index=0;
				}
				cnt++;
			}
			
			if(cnt==4) {
				break;
			}
		}

		System.out.println(x+" "+y);
	}

}
