"""Модели данных."""

from pydantic import BaseModel, Field


class Hypertable(BaseModel):
    """Metadata information about hypertables."""

    hypertable_schema: str = Field(description="Schema name of the hypertable")
    hypertable_name: str = Field(description="Table name of the hypertable")
    owner: str = Field(description="Owner of the hypertable")
    num_dimensions: int = Field(description="Number of dimensions")
    num_chunks: int = Field(description="Number of chunks")
    compression_enabled: bool = Field(
        description="Is compression enabled on the hypertable?",
    )
    is_distributed: bool = Field(description="Is the hypertable distributed?")
    replication_factor: int | None = Field(
        description="Replication factor for a distributed hypertable",
    )
    data_nodes: str | None = Field(
        description="Nodes on which hypertable is distributed",
    )
    tablespaces: str | None = Field(
        description="Tablespaces attached to the hypertable",
    )


class HypertableDetailedSize(BaseModel):
    """Get detailed information about disk space used by a hypertable."""

    table_bytes: int = Field(
        description=(
            "Disk space used by main_table (like pg_relation_size(main_table))"
        ),
    )
    index_bytes: int = Field(
        description="Disk space used by indexes",
    )
    toast_bytes: int = Field(
        description="Disk space of toast tables",
    )
    total_bytes: int = Field(
        description="Total disk space used by the specified table, "
        + "including all indexes and TOAST data",
    )
    node_name: str | None = Field(
        description="For distributed hypertables, this is the user-given name "
        + "of the node for which the size is reported. NULL is returned "
        + "for the access node and non-distributed hypertables.",
    )
