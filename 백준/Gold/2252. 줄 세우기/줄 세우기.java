import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

class Student{
	int sNo;
	public Student() {
	}
	public Student(int sNo) {
		this.sNo = sNo;
	}
	List<Student> income = new ArrayList<>();
	List<Student> outcome = new ArrayList<>();	
}

public class Main {
	

	public static void main(String[] args) {
		//(행렬로 받고
		//앞에 몇명있는지 기록 P(x)=N-x로 기록
		//x 앞에 있는 수는 P(x)-1로 기록
		//들어가 있는 순서대로 기록)
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		Student[] students = new Student[N];
		for(int i=0; i<N; i++) {
			students[i] = new Student(i);
		}
		
		for(int i=0; i<M; i++) {
			int p = sc.nextInt()-1;
			int q = sc.nextInt()-1;
			students[p].outcome.add(students[q]);
			students[q].income.add(students[p]);
		}
		
		int[] incomeArr = new int[N];
		boolean[] incomeArrVisit = new boolean[N]; 
		Queue<Student> queue = new LinkedList<>();
		for(int i=0; i<N; i++) {
			incomeArr[i]=students[i].income.size();
			if(incomeArr[i]==0) {
				queue.add(students[i]);
				incomeArrVisit[i]=true;
			}
		}
		
		while(!queue.isEmpty()) {
			Student student = queue.poll();
			System.out.print((student.sNo+1)+" ");
			for(int i=0; i<student.outcome.size(); i++) {
				student.outcome.get(i).income.remove(student);
				incomeArr[student.outcome.get(i).sNo]--;
			}
			
			for(int i=0; i<N; i++) {
				if(incomeArr[i]==0&&!incomeArrVisit[i]) {
					queue.add(students[i]);
					incomeArrVisit[i]=true;
				}
			}
			
			
		}

	}

}
