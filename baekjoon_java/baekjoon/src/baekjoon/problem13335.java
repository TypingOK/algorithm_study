package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class problem13335 {
	public static class truck {
		int a;
		int t;

		public truck(int a, int t) {
			this.a = a;
			this.t = t;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int w = Integer.parseInt(str[1]);
		int l = Integer.parseInt(str[2]);

		ArrayList<truck> t = new ArrayList<>();
		int[] b = new int[n];

		str = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			b[i] = Integer.parseInt(str[i]);
		}

		int end = 0;

		int time = 0;

		while (end < n || !t.isEmpty()) {
			time++;
			int weight = 0;
			int size = t.size();
			for (int i = 0; i < size; i++) {
				t.get(i).t++;
			}

			if (size > 0) {
				if (t.get(0).t > w) {
					t.remove(0);
				}
			}
			if (end < n) {
				size = t.size();

				if (size < w) {
					for (int i = 0; i < size; i++) {
						weight += t.get(i).a;
					}

					if (weight + b[end] <= l) {
						t.add(new truck(b[end++], 1));
					}
				}
			}

		}

		System.out.println(time);
	}

}
