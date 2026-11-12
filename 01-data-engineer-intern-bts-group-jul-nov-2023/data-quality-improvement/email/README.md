# Email Format Data Quality

**Scope:** normalize email text and validate its basic structure.

**Approach:** trim surrounding whitespace, normalize text consistently, inspect the local-part/domain structure, and flag values that fail a format rule for review. A syntax check does not prove that a mailbox exists or belongs to a particular person.

**Public example:** uses reserved example addresses only; no real email addresses or domain lists are included.

This page describes the category-level method and does not reproduce the submitted code.

---

## ภาษาไทย

# การตรวจรูปแบบ Email

**ขอบเขต:** ปรับข้อความ email ให้เป็นรูปแบบมาตรฐานและตรวจโครงสร้างเบื้องต้น

**แนวทาง:** ตัดช่องว่างหัวท้าย ปรับตัวอักษรให้สม่ำเสมอ ตรวจส่วนชื่อผู้ใช้และโดเมน และทำเครื่องหมายค่าที่ไม่ผ่านกฎรูปแบบเพื่อทบทวน การตรวจ syntax ไม่ได้ยืนยันว่ากล่องจดหมายมีอยู่จริงหรือเป็นของบุคคลใด

**ตัวอย่างสาธารณะ:** ใช้เฉพาะที่อยู่อีเมลสำหรับตัวอย่างที่สงวนไว้ ไม่มีอีเมลจริงหรือรายการโดเมนขององค์กร

หน้านี้อธิบายวิธีระดับหมวดโดยไม่ทำซ้ำโค้ดที่ส่งมอบ
