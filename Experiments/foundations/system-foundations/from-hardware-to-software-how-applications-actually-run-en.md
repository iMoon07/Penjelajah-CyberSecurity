# From Hardware to Software: How Applications Actually Run

[🇮🇩 Baca dalam Bahasa Indonesia](from-hardware-to-software-how-applications-actually-run-id.md)  
[🇲🇾 Baca dalam Bahasa Melayu](from-hardware-to-software-how-applications-actually-run-ms.md)  
[🇵🇭 Basahin sa Tagalog](from-hardware-to-software-how-applications-actually-run-tl.md)

﷽

![From Hardware to Software: How Applications Actually Run](from-hardware-to-software.png)

## A Simple Question: How Does a File Actually Run?

Have you ever wondered how clicking an app instantly opens a window on your screen?

We click an icon. A few moments later, buttons can be pressed, text can be typed, and images appear. What we see is just the interface. Behind the scenes, there's a lot more going on than meets the eye.

This article breaks down that process conceptually. It's not about becoming a hardware engineer, but about building a big-picture understanding of how applications actually run.

## Program vs Process: What's the Difference?

Before going further, it's important to distinguish these two terms:

- **Program** — A file stored on disk (e.g., `firefox`, `chrome.exe`, or an app binary). It's just a collection of instructions in data form. While it's sitting on disk unused, it's "inactive" — just code.
- **Process** — A program that is currently being executed. The moment you launch it, the operating system turns that program into a process. A process has its own memory space, current state, open files, and allocated resources.

**Simple analogy:** A program is a recipe written in a cookbook. A process is the actual dish being cooked in the kitchen. The recipe can sit on the shelf forever, but the dish only exists once you start cooking.

## The Layers of a Computer: Hardware, Operating System, and Application

For an application to run, three main layers work together:

| Layer | Role | Analogy |
| --- | --- | --- |
| **Hardware** | The physical parts: CPU, RAM, storage (SSD/HDD), GPU, and input/output devices. | Kitchen equipment: stove, counter, pots, and knives. |
| **Operating System (OS)** | The manager and mediator. It manages resources, grants access to hardware, schedules processes, and keeps applications isolated from each other. | The head chef. Decides who gets to use the stove, keeps things organized, and prevents chaos. |
| **Application (User Space)** | What we use directly: browsers, text editors, games, etc. Apps don't talk to hardware directly — they go through the OS. | The recipe and the dish you're trying to make. |

Key point: **Applications rarely talk directly to hardware.** They request what they need from the operating system through *system calls*.

## The Journey of an App: From Click to Screen

Let's follow the process step by step.

### Step 1: Request to Run the Program
You click the app icon. The executable file on disk (e.g., in `/usr/bin/` or `Program Files/`) is selected to run.

### Step 2: The OS Creates a Process
The OS reads the program file and:

- **Creates a new process** — Assigns it a unique ID (PID).
- **Allocates memory** — Sets aside space in RAM for code, data, and its needs.
- **Sets up context** — Determines which user is running it, its permissions, and which resources it's allowed to use.

### Step 3: Load from Disk to RAM
Programs are stored on slower media (SSD/HDD). To run efficiently, the OS loads only the necessary parts into **RAM**.

Why RAM? Because the CPU can access RAM much faster than disk. This is why apps feel sluggish when RAM is full and the system has to swap to disk.

### Step 4: The CPU Executes Instructions
Now the **CPU** gets to work. It fetches instructions from memory one by one, decodes them, and executes them.

Think of the CPU as a chef who only works off the "prep counter" (RAM). It doesn't keep running back to the pantry (disk) for every single ingredient. The pantry is for long-term storage, the counter is for active work.

### Step 5: Interacting Through System Calls
When an app needs something outside its own scope — like opening a file, connecting to the internet, or drawing to the screen — it asks the OS for help via a *system call*.

Examples:
- **Opening a file** → The app asks the OS to read a file from disk.
- **Drawing a window** → The app asks the OS (via the window manager) to display something on screen.
- **Saving data** → The app asks the OS to write data to storage.

The OS checks permissions and routes the request to the appropriate hardware.

### Step 6: The Result Appears on Screen
After all of this, what you requested appears. A button shows up, a webpage renders, or an error message is displayed.

All of this can happen in milliseconds, even though dozens or hundreds of tiny steps are involved.

## Why Do We Need an Operating System?

If apps could talk directly to hardware, it'd seem efficient. In reality, it'd be chaos.

The OS exists for these reasons:

- **Abstraction** — Apps don't need to know your exact RAM specs, SSD type, or GPU driver. The OS provides a consistent interface.
- **Resource management** — If ten apps want CPU time at once, the OS shares it fairly so everything runs smoothly.
- **Isolation** — One app's process shouldn't be able to freely read another app's memory. This is crucial for stability and security.
- **Security & permissions** — The OS decides what files an app can access, what it can connect to, and what it cannot.
- **Efficiency** — The OS is smart about what to load, what to defer, and how to make the best use of limited resources.

Without an OS, every app would need to understand every piece of hardware in the world. With an OS, apps only need to understand the OS.

## A Quick Look at the Memory Hierarchy

Before moving to the next article, here's a simple view of how memory is layered:

| Component | Speed | Size | Purpose |
| --- | --- | --- | --- |
| **Registers** | Fastest | Tiny (bytes) | Hold data the CPU is actively working with right now. |
| **CPU Cache (L1/L2/L3)** | Very fast | Small | Caches frequently used data/instructions so the CPU doesn't have to go to RAM as often. |
| **RAM (Main Memory)** | Fast | Medium–Large (GB) | Holds code, variables, and data for active processes. |
| **Storage (SSD/HDD)** | Slower | Very large (GB–TB) | Long-term storage for programs, files, and data. |

The rule is simple: **The closer to the CPU, the faster and smaller. The farther away, the slower but larger.**

## Conclusion

In short: **A program is not a process.** A program is a file sitting on disk. A process is that program brought to life in RAM and executed by the CPU.

The flow looks like this: *click → OS creates a process → load into RAM → CPU executes instructions → ask OS for help when needed → result appears on screen*.

The most important takeaway isn't memorizing chip specs, but this big picture: apps don't touch hardware directly. The operating system acts as a bridge, RAM acts as the "workbench", and the CPU does the actual work.

Understanding this mental model makes everything that comes next — memory, system calls, performance, and more — much easier to grasp.

## References

- Silberschatz, A., Galvin, P. B., & Gagne, G. *Operating System Concepts* (10th Edition) — Covers processes, memory management, and the role of the operating system. [Official Book Page](https://www.wiley.com/en-us/shop/general-end-user-computing/operating-system-concepts-10th-edition-p-9781119800361) · [Supplementary Resources](https://codex.cs.yale.edu/avi/os-book/OS10/index.html)

- Bryant, R. E., & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective (CS:APP)* (3rd Edition) — An excellent resource for understanding the relationship between hardware and software, including program execution and memory hierarchy. [Official Book Website](https://csapp.cs.cmu.edu/)

- Tanenbaum, A. S., & Bos, H. *Modern Operating Systems* (5th Edition) — Explains operating system concepts, process management, memory management, and how the OS mediates between applications and hardware.