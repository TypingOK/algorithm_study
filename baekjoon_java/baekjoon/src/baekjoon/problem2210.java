package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class problem2210 {
	static int N;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static List<String> p;
	public static void main(String[] args) throws IOException{
		int[][] map;
		int[] select;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		map = new int[5][5];
		for(int i=0; i<5; i++) {
			String[] str = br.readLine().split(" ");
			for(int j=0; j<5; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		N=0;
		select=new int[6];
		p = new ArrayList<>();
		for(int i=0; i<5; i++) {
			for(int j=0; j<5; j++) {
				DFS(i,j,0,map,select);
				
			}
		}
		System.out.println(N);
	}
	static void DFS(int x, int y, int cnt,int[][] map,int[] select) {
		if(cnt==6) {
			String str="";
			for(int i=0; i<6; i++) {
				str+=Integer.toString(select[i]);
			}
			int size=p.size();
			boolean flag=false;
			for(int i=0; i<size; i++) {
				if(p.get(i).equals(str)) {
					flag=true;
					break;
				}
			}
			if(flag) {
				return;
			}
			else {
				N++;
				p.add(str);
				return;
			}
		}
		
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			
			if(0<=nx && nx<5 && 0<=ny && ny<5) {
				select[cnt]=map[nx][ny];
				DFS(nx,ny,cnt+1,map,select);
			}
		}
		
	}

}
