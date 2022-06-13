package baekjoon;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class problem16509 {

	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, -1, 0, 1 };
	static int d1Lx[] = { -1, -1 };
	static int d1Ly[] = { -1, 1 };
	static int[] d2Lx = { -1, 1 };
	static int[] d2Ly = { -1, -1 };
	static int[] d3Lx = { 1, 1 };
	static int[] d3Ly = { -1, 1 };
	static int[] d4Lx = { -1, 1 };
	static int[] d4Ly = { 1, 1 };
	static int[][] map;
	static int answer;
	static boolean visit[][];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		answer = Integer.MAX_VALUE;
		map = new int[10][9];
		int a = sc.nextInt();
		int b = sc.nextInt();
		map[a][b] = 1;
		int c = sc.nextInt();
		int d = sc.nextInt();
		map[c][d] = 2;
		visit = new boolean[10][9];

		bfs(a, b);

		System.out.println(answer);
	}

	static void bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { x, y, 0 });

		visit=new boolean[10][9];
		visit[x][y]=true;
		

		while (!q.isEmpty()) {
			int temp[] = q.poll();
			if(map[temp[0]][temp[1]]==2) {
				answer = temp[2];
				return ;
			}
			for (int i = 0; i < 4; i++) {
				int nx = temp[0]+dx[i];
				int ny = temp[1]+dy[i];
				if(0<=nx && nx<10 && 0<=ny && ny<9 &&  map[nx][ny] !=2) {
					if(i==0) {
						for(int j=0; j<2; j++) {
							int kx=nx;
							int ky = ny;
							kx+=d1Lx[j];
							ky+=d1Ly[j];
							if(0<=kx && kx<10 && 0<=ky && ky<9 && map[kx][ky] !=2) {
								kx+=d1Lx[j];
								ky+=d1Ly[j];
								if(0<=kx && kx<10 && 0<=ky && ky<9 && !visit[kx][ky]) {
									visit[kx][ky] = true;
									q.add(new int[] {kx,ky,temp[2]+1});
								}
							}
						}
					}
					else if(i==1) {
						for(int j=0; j<2; j++) {
							int kx=nx;
							int ky = ny;
							kx+=d2Lx[j];
							ky+=d2Ly[j];
							if(0<=kx && kx<10 && 0<=ky && ky<9 && map[kx][ky] !=2) {
								kx+=d2Lx[j];
								ky+=d2Ly[j];
								if(0<=kx && kx<10 && 0<=ky && ky<9 && !visit[kx][ky]) {
									visit[kx][ky] = true;
									q.add(new int[] {kx,ky,temp[2]+1});
								}
							}
						}
					}
					else if(i==2) {
						for(int j=0; j<2; j++) {
							int kx=nx;
							int ky = ny;
							kx+=d3Lx[j];
							ky+=d3Ly[j];
							if(0<=kx && kx<10 && 0<=ky && ky<9 && map[kx][ky] !=2) {
								kx+=d3Lx[j];
								ky+=d3Ly[j];
								if(0<=kx && kx<10 && 0<=ky && ky<9 && !visit[kx][ky]) {
									visit[kx][ky] = true;
									q.add(new int[] {kx,ky,temp[2]+1});
								}
							}
						}
					}
					else if(i==3) {
						for(int j=0; j<2; j++) {
							int kx=nx;
							int ky = ny;
							kx+=d4Lx[j];
							ky+=d4Ly[j];
							if(0<=kx && kx<10 && 0<=ky && ky<9 && map[kx][ky] !=2) {
								kx+=d4Lx[j];
								ky+=d4Ly[j];
								if(0<=kx && kx<10 && 0<=ky && ky<9 && !visit[kx][ky]) {
									visit[kx][ky] = true;
									q.add(new int[] {kx,ky,temp[2]+1});
								}
							}
						}
					}
					
				}
				
			}
		}
		
		answer  =-1;
		return;
	}
}
