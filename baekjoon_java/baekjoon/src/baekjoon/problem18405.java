package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

import static java.lang.Integer.parseInt;

public class problem18405 {
    static int N;
    static int K;
    static int S;
    static int X;
    static int Y;
    static int[][] graph;
    static ArrayList<int[]> position;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        N = parseInt(str[0]);
        K = parseInt(str[1]);

        graph = new int[N][N];
        position = new ArrayList<>();

        for(int i=0; i<N; i++){
            str = br.readLine().split(" ");
            for(int j=0; j<N; j++){
                int result = parseInt(str[j]);
                graph[i][j] = result;
                if (result>0){
                    position.add(new int[] {i,j,result});
                }

            }
        }

        position.sort((o1, o2) -> {
            return o1[2] - o2[2];
        });

        str= br.readLine().split(" ");
        S = parseInt(str[0]);
        X = parseInt(str[1]);
        Y = parseInt(str[2]);

        int answer = BFS(S,X,Y);
        System.out.println(answer);

    }

    static int BFS(int S, int X, int Y){
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};

        Queue<int[]> q = new LinkedList<>();
        for (int[] ints : position) {
            q.offer(ints);
        }

        int count = 0;
        while(!q.isEmpty()){
            if (count < S){
                int size = q.size();
                for(int i=0; i<size; i++){
                    int[] temp = q.poll();
                    for(int j = 0; j<4; j++){
                        int nx = temp[0] + dx[j];
                        int ny = temp[1] + dy[j];

                        if (0<=nx && nx<N && 0<=ny && ny<N && graph[nx][ny] == 0){
                            q.offer(new int[] {nx,ny});
                            graph[nx][ny] = graph[temp[0]][temp[1]];
                        }
                    }
                }
                count++;
            }else{
                return graph[X-1][Y-1];
            }
        }
        return graph[X-1][Y-1];
    }
}
