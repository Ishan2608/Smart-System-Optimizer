from google import genai
import psutil
import platform
from core import GEMINI_API_KEY, GEMINI_MODEL_NAME
import os

class AIClient:
    def __init__(self, api_key=GEMINI_API_KEY, model_name=GEMINI_MODEL_NAME):
        """Initializes the AI client with the API key and model name."""
        self.api_key = api_key
        self.model = model_name
        self.client = genai.Client(api_key=self.api_key)
        self.chat = self.client.chats.create(model=self.model)
        self.system_profile = self._get_system_profile()

        # Initialize chat with role and instructions
        self._initialize_chat_with_role()

    def _initialize_chat_with_role(self):
        """Sends a system prompt to define the AI's role and behavior."""
        system_prompt = (
            "You are SysSKY, an AI assistant developed by Ishan Rastogi.\n"
            "Your purpose is to help users understand, optimize, and troubleshoot their systems.\n"
            "You have access to real-time system information such as CPU usage, RAM, Disk, Processes, and more.\n"
            "Use this data to give clear, actionable advice.\n"
            "Always respond in a helpful, professional tone.\n"
            "Do not make up data — only use what's provided in the system profile or user input.\n"
            "Start by welcoming the user and offering assistance."
        )
        try:
            # Send the system prompt as an initial message from the user
            self.chat.send_message(system_prompt)
        except Exception as e:
            print(f"Error initializing chat with role: {e}")

    def _get_system_profile(self):
        """Collects system information to create a profile."""
        profile = {
            "os": platform.system(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "platform": platform.platform(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "hostname": platform.node(),
            "python_version": platform.python_version(),
            "cpu": {
                "count_physical": psutil.cpu_count(logical=False),
                "count_logical": psutil.cpu_count(logical=True),
                "load_average": os.getloadavg() if hasattr(os, 'getloadavg') else "Not available"
            },
            "memory": {
                "total_ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
                "swap_total_gb": round(psutil.swap_memory().total / (1024 ** 3), 2)
            },
            "disk": self._get_detailed_disk_info(),
            "network": self._get_detailed_network_info()
        }
        return profile

    def _get_detailed_disk_info(self):
        """Retrieves detailed disk information for all partitions."""
        disk_info = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append({
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "fstype": partition.fstype,
                    "total_gb": round(usage.total / (1024 ** 3), 2),
                    "used_gb": round(usage.used / (1024 ** 3), 2),
                    "free_gb": round(usage.free / (1024 ** 3), 2),
                    "percent_used": usage.percent
                })
            except PermissionError:
                disk_info.append({
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "error": "PermissionError"
                })
            except Exception as e:
                disk_info.append({
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "error": str(e)
                })
        return disk_info

    def _get_detailed_network_info(self):
        """Retrieves detailed network interface information."""
        net_info = {}
        for nic, addresses in psutil.net_if_addrs().items():
            net_info[nic] = []
            for addr in addresses:
                net_info[nic].append({
                    "family": addr.family.name if hasattr(addr.family, 'name') else str(addr.family),
                    "address": addr.address,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast,
                    "ptp": addr.ptp
                })
        return net_info

    def get_response(self, prompt):
        """Sends a prompt to the AI model, including system profile and history."""
        augmented_prompt = f"System Info: {self.system_profile}. User Question: {prompt}"
        try:
            response = self.chat.send_message(augmented_prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def reset_chat(self):
        """Clears the chat history by creating a new chat object."""
        self.chat = self.client.chats.create(model=self.model)
        self._initialize_chat_with_role()  # Re-initialize after reset

    def get_chat_history_for_display(self):
        """Retrieves the chat history for display in the GUI."""
        history_text = ""
        for message in self.chat.history:
            role = message.role.capitalize()
            if role == "Ai":
                role = "SysSKY"
            content = message.parts[0].text if message.parts else ""
            history_text += f"{role}: {content}\n"
        return history_text