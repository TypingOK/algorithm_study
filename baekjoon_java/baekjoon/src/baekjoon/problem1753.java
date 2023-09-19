package baekjoon;

import java.util.*;
import java.io.*;

import static java.lang.Integer.parseInt;

public class problem1753 {
    static int V;
    static int E;
    static int K;
    static LinkedList<Node>[] graph;
    static int[] distance;

    static class Node implements Comparable<Node>{
        int to;
        int weight;

        Node(int to, int weight){
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o2) {
            return this.weight - o2.weight;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        V = parseInt(str[0]);
        E = parseInt(str[1]);
        str = br.readLine().split(" ");
        K = parseInt(str[0]);
        distance = new int[V+1];
        for(int i =0; i<V+1; i++){
            distance[i] = Integer.MAX_VALUE;
        }
        graph = new LinkedList[V+1];
        for(int i = 0; i<=V; i++){
            graph[i] = new LinkedList<>();
        }

        for(int i=0; i<E; i++){
            str = br.readLine().split(" ");
            int to = parseInt(str[0]);
            int from = parseInt(str[1]);
            int weight = parseInt(str[2]);
            graph[to].add(new Node(from,weight));
        }
        dijkstra();

        for(int i =1; i<V+1; i++){
            if(distance[i] == Integer.MAX_VALUE){
                System.out.println("INF");
            }else{
                System.out.println(distance[i]);
            }
        }
    }

    public static void dijkstra(){
//        Queue<Integer> q = new LinkedList<>();
        PriorityQueue<Node> q = new PriorityQueue<>();
        q.offer(new Node(K,0));

        distance[K] = 0;

        while(!q.isEmpty()){
            Node cur = q.poll();

            if(cur.weight > distance[cur.to]){
                continue;
            }

            for(Node node: graph[cur.to]){
                if(distance[node.to] > node.weight + cur.weight){
                    distance[node.to] = node.weight + cur.weight;
                    q.offer(new Node(node.to, node.weight+cur.weight));
                }
            }
        }
    }

}
