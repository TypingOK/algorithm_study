package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class problem1953 {
	static int N;
	static int M;
	static int [][] map;
	static boolean [][] visited;
	static int L;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static int answer;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		String str[];
		for(int tc=1; tc<=TC; tc++) {
			str= br.readLine().split(" ");
			N = Integer.parseInt(str[0]);
			M = Integer.parseInt(str[1]);
			int R = Integer.parseInt(str[2]);
			int C = Integer.parseInt(str[3]);
			L = Integer.parseInt(str[4]);
			
			map = new int[N][M];
			visited = new boolean[N][M];
			
			for(int i=0; i<N; i++) {
				str = br.readLine().split(" ");
				for(int j=0; j<M; j++) {
					map[i][j] = Integer.parseInt(str[j]);
				}
			}
			answer=0;
			dfs(R,C);
			
			
			for(int i=0;i<N; i++) {
				for(int j=0; j<M; j++) {
					if(visited[i][j]) {
						answer++;
					}
				}
			}
			System.out.println("#"+tc+" "+answer);
		}
	}
	
	static void dfs(int r, int c) {
		visited[r][c] = true;
		Queue<int[]> q = new LinkedList<int[]>();

		q.add(new int[] { r, c });
		int cnt = 1;
		while (!q.isEmpty()) {
			int size = q.size();
			if(cnt==L) {
				break;
			}
			for (int t = 0; t < size; t++) {

				int[] temp = q.poll();
				int x = temp[0];
				int y = temp[1];
//				print();

				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];

					if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny] && map[nx][ny] > 0) {
						if (i == 0) {
							if (map[x][y] == 1 || map[x][y] == 2 || map[x][y] == 5 || map[x][y] == 6) {
								if (map[nx][ny] == 1 || map[nx][ny] == 2 || map[nx][ny] == 4 || map[nx][ny] == 7) {
									visited[nx][ny] = true;
									q.add(new int[] { nx, ny });
								}
							}
						} else if (i == 1) {
							if (map[x][y] == 1 || map[x][y] == 3 || map[x][y] == 4 || map[x][y] == 5) {
								if (map[nx][ny] == 1 || map[nx][ny] == 3 || map[nx][ny] == 6 || map[nx][ny] == 7) {
									visited[nx][ny] = true;
									q.add(new int[] { nx, ny });
								}
							}
						} else if (i == 2) {
							if (map[x][y] == 1 || map[x][y] == 2 || map[x][y] == 4 || map[x][y] == 7) {
								if (map[nx][ny] == 1 || map[nx][ny] == 2 || map[nx][ny] == 5 || map[nx][ny] == 6) {
									visited[nx][ny] = true;
									q.add(new int[] { nx, ny });
								}
							}
						} else if (i == 3) {
							if (map[x][y] == 1 || map[x][y] == 3 || map[x][y] == 6 || map[x][y] == 7) {
								if (map[nx][ny] == 1 || map[nx][ny] == 3 || map[nx][ny] == 4 || map[nx][ny] == 5) {
									visited[nx][ny] = true;
									q.add(new int[] { nx, ny });
								}
							}
						}
					}
				}
			}
			cnt++;
		}
	}
	static void print() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j]) {
                    switch (map[i][j]) {
                    case 1:
                        System.out.print("┼ ");
                        break;
                    case 2:
                        System.out.print("│ ");
                        break;
                    case 3:
                        System.out.print("─ ");
                        break;
                    case 4:
                        System.out.print("└ ");
                        break;
                    case 5:
                        System.out.print("┌ ");
                        break;
                    case 6:
                        System.out.print("┐ ");
                        break;
                    case 7:
                        System.out.print("┘ ");
                        break;
                    default:
                        System.out.print("○ ");
                    }
                } else
                    System.out.print("X ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("--------------------------------------------------");
        System.out.println();
    }

}
//5 6 2 1 3
//0 0 5 3 6 0
//0 0 2 0 2 0
//3 3 1 3 7 0
//0 0 0 0 0 0
//0 0 0 0 0 0
