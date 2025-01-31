B
    ��z]V   �               @   s   d dl mZmZ d dlmZ d dlZd dlmZ d dlm	Z	 d dlmZ d dl
Z
d dlZd dlZdZdZe
�d�Zg Zd	ekr�d
ed	< dekr�g ed< dekr�ded< eed�Zee�Zddd�Zdd� Zed fdd�ZdZdd� Zdd� Zedkr�e�  dS )�    )�LINE�OEPoll)�
execute_jsN)�TalkException)�ProcesszWIN10	5.9.0	SpamJS	12zDESKTOPMAC	5.11.1	SpamJS	12zsettings_f.json�token�#�contact�nameu,   @ɪɴᴠɪᴛᴇᴇ:ឆាุఐণ௫ণఐ)�appNameF)�get�removec             C   s   t d| � ��S )Nzspamadd.js uid=)r   )Zuid� r   �
loginme.py�runadd   s    r   c             C   s8  |g krdS yt | ttd�}W n   t�| d� dS |�� jdkrT|�| d� dS d�|j|jj	t
d �� �}dd	� |�|�D �}|�� }x�|D ]�}||k�ry|�|� W n^   y|�| d
�|�� W n: tk
�r } z|jdkr�t�| d�S W d d }~X Y nX Y nX |d�|�7 }q�W t|� t�| d� d S )NF)Z_toZ_clientr   u0   ล็อกอินไม่สำเร็จTuL   กรุณาปิด Letter Sealing ก่อนทำการรันzspam.js token={} mid={} name={}r
   c             S   s   g | ]
}|j �qS r   )�mid)�.0�cr   r   r   �
<listcomp>&   s    zstart_run.<locals>.<listcomp>zUnable to add contact. {})�   �   �   uH   กรุณาล็อกอินใหม่อีกครั้งz uid={}z [@invitee:NOTIF]
Done operation.)r   �exg�appJS�sendMessageZgetSettingsZ
e2eeEnable�formatZ	authTokenZprofiler   �settings�strip�getContactsZgetAllContactIdsZfindAndAddContactsByMid�TalkE�coder   )�toZcontactsZclient�cmdZparsed_listZfriendsr   �errr   r   r   �	start_run   s8     


r$   uD  คำสั่งทั้งหมดของ @INVITEE #Beta
@invitee:help
@invitee:contact ~ เช็คคท.
@invitee:getmode ~ เปิด/ปิดการรับคอนแทค
@invitee:removemode ~ เปิด/ปิดการลบคอนแทค
@invitee:check [เลข] ~ เช็คคท.ในรายชื่อ
@invitee:remove [เลข] ~ ลบคท.ในรายชื่อ
@invitee:runadd [เลข] ~ รันแอดคท.ในรายชื่อ
@invitee:setname [ชื่อที่ต้องการ] ~ เปลี่ยนชื่อห้องรัน
@invitee:login ~ ล็อกอิน
*** เมื่อลบแล้ว จะทำให้เลขคลาดเคลื่อนได้ กรุณาเช็คเลขอีกครั้ง*** c             C   s�  | j }|jdkrd S |jdkr"d S |jdk�r4|j�� }|dk�r.td g krRd S d}g }x6td D ]*}yt�|� W qd   |�|� Y qdX qdW x|D ]}td �	|� q�W |g kr�t�
|jd�tt|���� d}x<dd	� t�td �D �D ] }|d
 }|d�t|�|�7 }q�W t�
|j|d d� � �n|dk�rFt|j� �n�|dk�rbt�
|jt� �n�|�d��r�|j�d�d
 }	yt|	�}	W n   t�
|jd�S ytd |	d
  }
W n   t�
|jd�S td |	d
  }t|� t�
|jd� �n@|�d��r�|j�d�d
 }	yt|	�}	W n   t�
|jd�S ytd |	d
  }
W n   t�
|jd�S t�td |	d
  �j}td �	td |	d
  � t�
|jd�|�� �n�|�d��r0|j�d�d
 }	yt|	�}	W n   t�
|jd�S ytd |	d
  }
W n   t�
|jd�S td |	d
  }t�|j|� �n|�d��r�|j�d�d
 �� }t|�dk�rpt�
|jd� d S |td< t�
|jd�td �� n�|dk�r�td �s�d nd!td< d!td"< td �r�t�
|jd#� nt�
|jd$� nP|d%k�r4td" �s�d nd!td"< d!td< td" �r&t�
|jd&� nt�
|jd'� |jd(k�r�td �r�|jd) td k�r�td �|jd) � t�
|jd*� td" �r�|jd) td k�r�td �	|jd) � t�
|jd+� d S ),N)r   �   �   r   z@invitee:contactr	   u@   ผู้ใช้ลบบัญชีจำนวน {} คนu#   บัญชีที่รัน:
c             S   s   g | ]
}|j �qS r   )�displayName)r   �mr   r   r   r   Y   s    zoperator.<locals>.<listcomp>�   z{}. {}
�����z@invitee:loginz@invitee:helpz@invitee:runadd � u*   ตัวเลขเท่านั้นuL   ไม่พบคท.ที่ต้องการจะรันแอดu   เรียบร้อยz@invitee:remove u@   ไม่พบคท.ที่ต้องการจะลบu3   ลบคท.ชื่อ {} ออกแล้ว!z@invitee:check u4   ไม่พบคท.ที่ต้องการz@invitee:setname �2   u3   ชื่อห้องยาวเกินไปr
   uS   เปลี่ยนชื่อห้องรันเป็น {} แล้ว!z@invitee:getmoder   TFr   u4   เปิดรับคอนแทคแล้ว!u0   ปิดรับคอนแทคแล้วz@invitee:removemodeu<   เปิดยกเลิกคอนแทคแล้วu9   ปิดยกเลิกคอนแทคแล้วr%   r   u   เพิ่มแล้วu6   ลบออกเรียบร้อยแล้ว)�messageZcontentTypeZtoType�text�lowerr   r   Z
getContact�appendr   r   r!   r   �str�lenr   r$   �help�
startswith�split�intr   r'   ZsendContactr   �setZcontentMetadata)�op�msgZmlowZnoZdel_listr   �dZstryr
   r5   �sr	   r   r   r   �operatorC   s�    
 
 




      

 

 

r<   c           
   C   s�   x�y�d} yt jdd�} W n0 tk
rH } ztd�|�� d S d }~X Y nX xD| D ]<}|jdkr�yt|� W n   t��  Y nX t �	|j
� qPW W q tk
r�   t��  Y q tk
r�   t�d� Y qX qW d S )N� r,   )�countz[TRACING ERR] {})�   �   r)   )�cPollZsingleTrace�	Exception�printr   �typer<   �	traceback�	print_excZsetRevisionZrevision�KeyboardInterrupt�sys�exit)Zops�er8   r   r   r   �start�   s*      

   rK   �__main__)ZMIGHTAPI.MIGHTLYr   r   ZNaked.toolshed.shellr   ZmultiprocessingZakad.ttypesr   r   r   ZlivejsonrE   rH   Zappr   ZFiler   �procr   rA   r7   r   r$   r3   r<   rK   �__name__r   r   r   r   �<module>   s4   


'Y