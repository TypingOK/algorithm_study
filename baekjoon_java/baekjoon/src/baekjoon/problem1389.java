package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

import static java.lang.Integer.parseInt;

public class problem1389 {
    static int N;
    static int M;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int min;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        N = parseInt(str[0]);
        M = parseInt(str[1]);
        graph = new ArrayList[N+1];
        min = Integer.MAX_VALUE;
        for(int i=0; i<N+1; i++){
            graph[i] = new ArrayList<>();
        }
        int answer = 0;

        for(int i=0; i<M; i++){
            str = br.readLine().split(" ");
            int A = parseInt(str[0]);
            int B = parseInt(str[1]);
            graph[A].add(B);
            graph[B].add(A);
        }
        for(int i=1; i<N+1; i++){
            visited = new boolean[N+1];
            int result = BFS(graph,visited,i);
            if(min > result){
                min = result;
                answer = i;
            }
        }
        System.out.println(answer);

    }

    static int BFS(ArrayList<Integer>[] graph, boolean[] visited,int start){
        Queue<int[]> q = new LinkedList<>();
        int count = 0;
        q.offer(new int[] {start,0});
        visited[start] = true;
        while (!q.isEmpty()){
            int[] temp = q.poll();
            count += temp[1];

            int size = graph[temp[0]].size();
            for(int i=0; i<size; i++){
                if (!visited[graph[temp[0]].get(i)]){
                    visited[graph[temp[0]].get(i)] = true;
                    q.offer(new int[] {graph[temp[0]].get(i),temp[1]+1});
                }
            }
        }
        return count;
    }
}
