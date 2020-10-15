using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace GenScenarios.Models
{
    public partial class ForensicsThesisContext : DbContext
    {
        public ForensicsThesisContext()
        {
        }

        public ForensicsThesisContext(DbContextOptions<ForensicsThesisContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Act> Act { get; set; }
        public virtual DbSet<Os> Os { get; set; }
        public virtual DbSet<OsAct> OsAct { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer("Server=tcp:forensicsthesis.database.windows.net,1433;Initial Catalog=ForensicsThesis;Persist Security Info=False;User ID=student;Password=HCMUS@1753002;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Act>(entity =>
            {
                entity.ToTable("ACT");

                entity.Property(e => e.Id).HasColumnName("ID");

                entity.Property(e => e.ActName)
                    .HasColumnName("ACT_NAME")
                    .HasMaxLength(100);
            });

            modelBuilder.Entity<Os>(entity =>
            {
                entity.ToTable("OS");

                entity.Property(e => e.Id).HasColumnName("ID");

                entity.Property(e => e.Architecture)
                    .HasColumnName("ARCHITECTURE")
                    .HasMaxLength(10)
                    .IsUnicode(false)
                    .IsFixedLength();

                entity.Property(e => e.Kernel)
                    .HasColumnName("KERNEL")
                    .HasMaxLength(50)
                    .IsUnicode(false)
                    .IsFixedLength();

                entity.Property(e => e.Memory).HasColumnName("MEMORY");

                entity.Property(e => e.OsName)
                    .HasColumnName("OS_NAME")
                    .HasMaxLength(50)
                    .IsUnicode(false)
                    .IsFixedLength();
            });

            modelBuilder.Entity<OsAct>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("OS_ACT");

                entity.Property(e => e.IdAct).HasColumnName("ID_ACT");

                entity.Property(e => e.IdOs).HasColumnName("ID_OS");

                entity.HasOne(d => d.IdActNavigation)
                    .WithMany()
                    .HasForeignKey(d => d.IdAct)
                    .HasConstraintName("FK_ID_ACT");

                entity.HasOne(d => d.IdOsNavigation)
                    .WithMany()
                    .HasForeignKey(d => d.IdOs)
                    .HasConstraintName("FK_ID_OS");
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
