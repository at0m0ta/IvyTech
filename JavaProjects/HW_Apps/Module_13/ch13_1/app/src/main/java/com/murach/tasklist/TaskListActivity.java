package com.murach.tasklist;

import java.util.ArrayList;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class TaskListActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_task_list);
        
        // get db and StringBuilder objects
        TaskListDB db = new TaskListDB(this);
        StringBuilder sb = new StringBuilder();
        
        // insert a task
        Task task = new Task(1, "Make dentist appointment", "", "0", "0");
        long insertId = db.insertTask(task);
        if (insertId > 0) {
            sb.append("Row inserted! Insert Id: " + insertId + "\n");
        }
        
        // insert a second task
        Task task2 = new Task(1, "Take car in for oil change", "", "0", "0");
        long insertId2 = db.insertTask(task2);
        if (insertId2 == 1) {
            sb.append("Row inserted! Insert Id: " + insertId2 + "\n");
        }

        // update a task
        task.setId((int) insertId);
        task.setName("Update test");
        int updateCount = db.updateTask(task);
        if (updateCount == 1) {
            sb.append("Task updated! Update count: " + updateCount + "\n");
        }
        
        // delete a task
        int deleteCount = db.deleteTask(insertId);
        if (deleteCount == 1) {
            sb.append("Task deleted! Delete count: " + deleteCount + "\n\n");
        }
        
        // delete old tasks
        db.deleteTask(4);
        db.deleteTask(5);
        db.deleteTask(6);
        db.deleteTask(7);
        db.deleteTask(8);
        db.deleteTask(9);
        db.deleteTask(10);
        db.deleteTask(11);
        db.deleteTask(12);
        db.deleteTask(13);
        db.deleteTask(14);
        db.deleteTask(15);
        db.deleteTask(16);
        db.deleteTask(17);
        db.deleteTask(18);

        
        // display all tasks (id + name)
        ArrayList<Task> tasks = db.getTasks("Personal");
        for (Task t : tasks) {
            sb.append(t.getId() + "|" + t.getName() + "\n");
        }
        
        // display string on UI
        TextView taskListTextView = (TextView) 
                findViewById (R.id.taskListTextView);
        taskListTextView.setText(sb.toString());
    }
}