exp 5 :
import java.util.*;
public class Main {

    // Function to find the maximum timestamp
// between 2 events
    static int max1(int a, int b)
    {
        // Return the greatest of the two
        if (a > b)
            return a;
        else
            return b;
    }

    // Function to display the logical timestamp
    static void display(int e1, int e2, int p1[], int p2[])
    {
        int i;
        System.out.print(
                "\nThe time stamps of events in P1:\n");

        for (i = 0; i < e1; i++) {
            System.out.print(p1[i] + " ");
        }

        System.out.println(
                "\nThe time stamps of events in P2:");

        // Print the array p2[]
        for (i = 0; i < e2; i++)
            System.out.print(p2[i] + " ");
    }

    // Function to find the timestamp of events
    static void lamportLogicalClock(int e1, int e2,
                                    int m[][])
    {
        int i, j, k;
        int p1[] = new int[e1];
        int p2[] = new int[e2];
        // Initialize p1[] and p2[]
        for (i = 0; i < e1; i++)
            p1[i] = i + 1;

        for (i = 0; i < e2; i++)
            p2[i] = i + 1;
        for (i = 0; i < e2; i++)
            System.out.print("\te2" + (i + 1));

        for (i = 0; i < e1; i++) {
            System.out.print("\n e1" + (i + 1) + "\t");
            for (j = 0; j < e2; j++)
                System.out.print(m[i][j] + "\t");
        }

        for (i = 0; i < e1; i++) {
            for (j = 0; j < e2; j++) {

                // Change the timestamp if the
                // message is sent
                if (m[i][j] == 1) {
                    p2[j] = max1(p2[j], p1[i] + 1);
                    for (k = j + 1; k < e2; k++)
                        p2[k] = p2[k - 1] + 1;
                }

                // Change the timestamp if the
                // message is received
                if (m[i][j] == -1) {
                    p1[i] = max1(p1[i], p2[j] + 1);
                    for (k = i + 1; k < e1; k++)
                        p1[k] = p1[k - 1] + 1;
                }
            }
        }

        // Function Call
        display(e1, e2, p1, p2);
    }

    public static void main(String args[])
    {
        int e1 = 5, e2 = 3;
        int m[][] = new int[5][3];
        // message is sent and received
        // between two process

	/*dep[i][j] = 1, if message is sent
					from ei to ej
		dep[i][j] = -1, if message is received
						by ei from ej
		dep[i][j] = 0, otherwise*/
        m[0][0] = 0;
        m[0][1] = 0;
        m[0][2] = 0;
        m[1][0] = 0;
        m[1][1] = 0;
        m[1][2] = 1;
        m[2][0] = 0;
        m[2][1] = 0;
        m[2][2] = 0;
        m[3][0] = 0;
        m[3][1] = 0;
        m[3][2] = 0;
        m[4][0] = 0;
        m[4][1] = -1;
        m[4][2] = 0;

        // Function Call
        lamportLogicalClock(e1, e2, m);
    }
}

cmd
input : javac main.java
java main

exp 6:
import java.util.Random;
import java.util.Scanner;

class Process {
    int id;
    boolean isActive;

    Process(int id) {
        this.id = id;
        this.isActive = true;
    }
}

public class Main {
    static Process[] processes;
    static int coordinator;

    public static void initiateElection(int initiator) {
        System.out.println("\nProcess " + initiator + " has initiated an election.");

        boolean higherProcessExists = false;

        for (Process process : processes) {
            if (process.id > initiator && process.isActive) {
                System.out.println("Process " + initiator + " sends election message to Process " + process.id);
                higherProcessExists = true;
            }
        }

        if (!higherProcessExists) {
            coordinator = initiator;
            announceCoordinator();
        }
    }

    public static void announceCoordinator() {
        System.out.println("\nProcess " + coordinator + " is the new coordinator.");
        for (Process process : processes) {
            if (process.id != coordinator && process.isActive) {
                System.out.println("Process " + coordinator + " sends coordinator message to Process " + process.id);
            }
        }
    }

    public static void failProcess(int id) {
        for (Process process : processes) {
            if (process.id == id) {
                process.isActive = false;
                System.out.println("Process " + id + " has failed.");
                if (coordinator == id) {
                    System.out.println("Coordinator has failed! Starting new election...");
                    startElection();
                }
                return;
            }
        }
        System.out.println("Process not found.");
    }

    public static void startElection() {
        for (int i = processes.length - 1; i >= 0; i--) {
            if (processes[i].isActive) {
                initiateElection(processes[i].id);
                break;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of processes: ");
        int n = scanner.nextInt();
        processes = new Process[n];

        System.out.println("\nAssigning process IDs...");
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            processes[i] = new Process(random.nextInt(100) + 1);
            System.out.println("Process ID: " + processes[i].id);
        }

        startElection();

        while (true) {
            System.out.print("\nEnter process ID to fail (or -1 to exit): ");
            int failId = scanner.nextInt();
            if (failId == -1) break;
            failProcess(failId);
        }
        scanner.close();
    }
}
input : 6

exp 7:
