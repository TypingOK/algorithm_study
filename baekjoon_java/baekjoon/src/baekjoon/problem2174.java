package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class problem2174 {
	
	static int N;
	static int M;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,-1,0,1};
	
	static int[][] map;
	static int rCount;
	static int order;
	static ArrayList<Robot> r;
	static int number;
	
	public static class Robot{
		int x;
		int y;
		int d;
		public Robot(int x, int y, String d){
			this.x = x;
			this.y = y;
			if(d.equals("N")) {
				this.d = 0;
			}else if(d.equals("W")) {
				this.d = 1;
			}else if(d.equals("S")) {
				this.d = 2;
			}else if(d.equals("E")) {
				this.d = 3;
			}
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		
		str = br.readLine().split(" ");
		
		rCount = Integer.parseInt(str[0]);
		order = Integer.parseInt(str[1]);
		
		r = new ArrayList<>();
		
		number = 0;
		
		map = new int[M+1][N+1];
		
		for(int i=0; i<rCount; i++) {
			str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			map[b][a] = i+1;
			r.add(new Robot(b,a,str[2]));
		}
		
		for(int i=0; i<order; i++) {
			str = br.readLine().split(" ");
			int num = Integer.parseInt(str[0]);
			String command = str[1];
			int f = Integer.parseInt(str[2]);
			
			
			int result = moving(num-1,command,f);
			
			if(result==1) {
				System.out.println("Robot "+ num +" crashes into the wall");
				System.exit(0);
			}else if(result == 2){
				System.out.println("Robot "+ num +" crashes into robot "+number);
				System.exit(0);
			}
			
			
		}
		
		System.out.println("OK");
	}

	
	public static int moving(int index,String command, int f) {
		
		Robot a = r.get(index);
		
		int x = a.x;
		int y = a.y;
		int d = a.d;
		
		
		if(command.equals("L")) {
			for(int i=0; i<f; i++) {
				if(d==0) {
					d = 1;
				}else if(d == 1) {
					d = 2;
				}else if(d == 2) {
					d = 3;
				}else {
					d = 0;
				}
				
			}
		}else if(command.equals("R")) {
			for (int i = 0; i < f; i++) {
				if (d - 1 < 0) {
					d = 3;
				} else {
					d -= 1;
				}
			}
			
		}else if(command.equals("F")) {
			for(int i=0; i<f; i++) {
				int nx = x+dx[d];
				int ny = y+dy[d];
				if(0<nx && nx <= M && 0<ny && ny<=N) {
					if(map[nx][ny] == 0) {
						map[nx][ny] = index+1;
						map[x][y] = 0;
						x = nx;
						y = ny;
					}else {
						number = map[nx][ny];
						return 2;
					}
				}else {
					return 1;
				}
			}
		}
		
		r.get(index).x = x;
		r.get(index).y = y;
		r.get(index).d = d;
		return 0;
	}
}
