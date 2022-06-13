package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class problem3055 {
	static int N;
	static int M;

	static int time;

	static int map[][];
	static int copy[][];
	static int dx[] = { 1, -1, 0, 0 };
	static int dy[] = { 0, 0, 1, -1 };
	static boolean visit[][];
	static Queue<int[]> q2 = new LinkedList<>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		visit = new boolean [N][M];
		time = 0;
		map = new int[N][M];
		copy = new int[N][M];
		int x = 0;
		int y = 0;
		for (int i = 0; i < N; i++) {
			char[] c = br.readLine().toCharArray();
			for (int j = 0; j < M; j++) {
				if (c[j] == 'D') {
					map[i][j] = 9;
				} else if (c[j] == '.') {
					map[i][j] = 0;
				} else if (c[j] == '*') {
					map[i][j] = 1;
					q2.add(new int[] { i, j });
				} else if (c[j] == 'S') {
					map[i][j] = 2;
					copy[i][j] = 2;
					x = i;
					y = j;
				} else if (c[j] == 'X') {
					map[i][j] = 3;
				}
			}
		}

		BFS(x, y);
		if (time == 0) {
			System.out.println("KAKTUS");
		} else {
			System.out.println(time);
		}

	}

	static void BFS(int x, int y) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] { x, y });
		int listSize = q2.size();

		while (!q.isEmpty()) {
			int size = q.size();
			for (int i = 0; i < size; i++) {
				int temp[] = q.poll();
				if (map[temp[0]][temp[1]] == 1) {
					continue;
				} else if (map[temp[0]][temp[1]] == 9) {
					return;
				}
				for (int j = 0; j < 4; j++) {
					int nx = temp[0] + dx[j];
					int ny = temp[1] + dy[j];

					if (0 <= nx && nx < N && 0 <= ny && ny < M && map[nx][ny] != 1 && map[nx][ny] != 3 && !visit[nx][ny]) {
						copy[temp[0]][temp[1]] = 0;
						copy[nx][ny] = 2;
						visit[nx][ny] = true;
						q.add(new int[] { nx, ny });
					}
				}
			}

			int lsize = q2.size();
			for (int i = 0; i < lsize; i++) {
				int temp[] = q2.poll();
				for (int j = 0; j < 4; j++) {
					int nx = temp[0] + dx[j];
					int ny = temp[1] + dy[j];
					if (0 <= nx && nx < N && 0 <= ny && ny < M &&map[nx][ny] != 1 && map[nx][ny] != 9 && map[nx][ny] != 3) {
						map[nx][ny] = 1;
						q2.add(new int[] { nx, ny });
					}
				}
			}
			time++;
		}

		time = 0;
		return;
	}

}
