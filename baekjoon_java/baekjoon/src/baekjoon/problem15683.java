package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class problem15683 {
	static int N;
	static int M;
	static int map[][];
	static int min;
	static ArrayList<int[]> list;
	static int[] cctv;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,-1,0,1};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		
		map = new int[N][M];
		
		list = new ArrayList<int[]>();
		cctv = new int[8];
		int index=0;
		min = Integer.MAX_VALUE;
		
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
				if(map[i][j]>0 && map[i][j]<6) {
					list.add(new int[] {i,j});
					cctv[index++] = map[i][j];
				}
			}
		}
		check(0,map,list.size());
		
		System.out.println(min);
		
	}
	
	public static void check(int depth,int mapCopy[][],int size) {
		if(depth == size) {
			int result = result(mapCopy);
			min = Math.min(result,min);
			return;
		}else {
			int temp[] = list.get(depth);
			int [][] mapArray = copy(mapCopy);
			for(int i=0; i<4; i++) {
				mapArray = mapCopy(mapArray,cctv[depth],i,temp[0],temp[1],0);
				check(depth+1,mapArray,size);
				mapArray = copy(mapCopy);
			}
		}
	}
	
	public static int result(int[][] mapCopy) {
		int count = 0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(mapCopy[i][j]==0) {
					count++;
				}
			}
		}
		return count;
	}
	
	public static int[][] copy(int[][] mapArray){
		int mapCopy[][] = new int[N][M];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				mapCopy[i][j] = mapArray[i][j];
			}
		}
		
		return mapCopy;
	}
	
	public static int[][] mapCopy(int mapCopy[][],int n,int d,int i, int j,int reverse){
		if(n==1) {
			return cctvNo1(mapCopy,d,i,j,reverse);
		}else if(n==2) {
			return cctvNo2(mapCopy,d,i,j,reverse);
		}else if(n==3) {
			return cctvNo3(mapCopy,d,i,j,reverse);
		}else if(n==4) {
			return cctvNo4(mapCopy,d,i,j,reverse);
		}else {
			return cctvNo5(mapCopy,i,j,reverse);
		}
	}
	
	public static int[][] cctvNo1(int mapCopy[][],int d,int i, int j,int reverse){
		int n=1;
		
		while(true) {
			int nx = i+ (dx[d] * n);
			int ny = j+ (dy[d] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==0 ) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}
			else {
				break;
			}
		}
		return mapCopy;
	}
	
	
	public static int[][] cctvNo2(int mapCopy[][],int d,int i, int j,int reverse){
		int n=1;
		
		while(true) {
			int nx = i+ (dx[d] * n);
			int ny = j+ (dy[d] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 && reverse == 0) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}
			else {
				break;
			}
		}
		
		n=1;
		d+=2;
		if(d>=4) {
			d=d%4;
		}
		while(true) {
			int nx = i+ (dx[d] * n);
			int ny = j+ (dy[d] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 && reverse == 0) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}
			else {
				break;
			}
		}
		return mapCopy;
	}
	
	
	public static int[][] cctvNo3(int mapCopy[][],int d,int i, int j,int reverse){
		int n=1;
		
		while(true) {
			int nx = i+ (dx[d] * n);
			int ny = j+ (dy[d] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 && reverse == 0 ) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}
			else {
				break;
			}
		}
		
		int dd = d+1;
		
		if(dd>=4) {
			dd=dd%4;
		}
		n=1;
		while(true) {
			int nx = i+ (dx[dd] * n);
			int ny = j+ (dy[dd] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 && reverse==0) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}else {
				break;
			}
		}
		
		return mapCopy;
	}
	
	
	public static int[][] cctvNo4(int mapCopy[][],int d,int i, int j,int reverse){
		int n=1;
		
		while(true) {
			int nx = i+ (dx[d] * n);
			int ny = j+ (dy[d] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 && reverse==0) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				System.out.println("!");
				mapCopy[nx][ny] = 0;
			}else {
				break;
			}
		}
		int dd = d+1;
		
		if(dd>=4) {
			dd=dd%4;
		}
		n=1;
		while(true) {
			int nx = i+ (dx[dd] * n);
			int ny = j+ (dy[dd] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 && reverse==0) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}else {
				break;
			}
		}
		
		
		n=1;
		d+=2;
		if(d>=4) {
			d=d%4;
		}
		while(true) {
			int nx = i+ (dx[d] * n);
			int ny = j+ (dy[d] * n);
			n++;
			if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse==0) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 9;
			}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
				if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
					continue;
				}
				mapCopy[nx][ny] = 0;
			}else {
				break;
			}
		}
		
		return mapCopy;
	}
	
	
	public static int[][] cctvNo5(int mapCopy[][],int i, int j,int reverse){
		for (int d = 0; d < 4; d++) {
			int n = 1;
			while (true) {
				int nx = i + (dx[d] * n);
				int ny = j + (dy[d] * n);
				n++;
				if (nx >= 0 && nx < N && ny >= 0 && ny < M && mapCopy[nx][ny] != 6 && reverse == 0) {
					if (mapCopy[nx][ny] > 1 && mapCopy[nx][ny] < 6) {
						continue;
					}
					mapCopy[nx][ny] = 9;
				}else if(nx>=0 && nx<N && ny>=0 && ny<M && mapCopy[nx][ny] !=6 &&reverse ==1) {
					if(mapCopy[nx][ny]>1 && mapCopy[nx][ny]<6) {
						continue;
					}
					mapCopy[nx][ny] = 0;
				} else {
					break;
				}
			}
		}
		return mapCopy;
	}
		
}
