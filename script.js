const API_URL = "http://127.0.0.1:5000/tasks";

function loadTasks() {

fetch(API_URL)
.then(response => response.json())
.then(tasks => {

let html = "";

tasks.forEach(task => {

html += `
<div class="task">

<h3>${task.title}</h3>

<p>${task.description}</p>

<p>Status: ${task.status}</p>

<button onclick="deleteTask(${task.id})">
Delete
</button>

</div>
`;

});

document.getElementById("taskList").innerHTML = html;

});

}

function addTask() {

const title =
document.getElementById("title").value;

const description =
document.getElementById("description").value;

fetch(API_URL, {

method: "POST",

headers: {
"Content-Type": "application/json"
},

body: JSON.stringify({
title,
description,
status:"Pending"
})

})
.then(response => response.json())
.then(() => {

document.getElementById("title").value="";
document.getElementById("description").value="";

loadTasks();

});

}

function deleteTask(id){

fetch(`${API_URL}/${id}`,{
method:"DELETE"
})
.then(() => loadTasks());

}

loadTasks();